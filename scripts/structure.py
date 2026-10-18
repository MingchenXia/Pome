"""Reviewed section boundaries, independent of source manuscript numbering."""
from copy import deepcopy
import re
from unidecode import unidecode


def title_key(value):
    value = re.sub(r"\\(?:mathcal|mathrm|mathbf|mathbb|operatorname)\s*\{([^{}]*)\}", r"\1", value)
    value = re.sub(r"\\(?:mathcal|mathrm|mathbf|mathbb)\s+([A-Za-z])", r"\1", value)
    return re.sub(r"[^a-z0-9]+", "", unidecode(value).casefold())


def arrange_sections(entries, topics, configuration):
    """Promote selected headings; keep the old subject as its introduction."""
    configuration = deepcopy(configuration)
    promoted = set()
    for original, promotions in configuration.get("section_promotions", {}).items():
        if original not in topics:
            raise ValueError(f"Missing section to subdivide: {original}")
        boundaries = {item["start"]: item for item in promotions}
        if len(boundaries) != len(promotions):
            raise ValueError(f"Repeated section boundary: {original}")
        current, seen = original, []
        for entry in entries.values():
            if entry["topic"] != original:
                continue
            variant = entry["variants"][0]
            if variant.get("section") and title_key(variant["caption"]) == title_key(topics[original]["title"]):
                current = original
            if entry["tag"] in boundaries:
                boundary = boundaries[entry["tag"]]
                if not entry["variants"][0].get("section"):
                    raise ValueError("A section boundary must be a source heading")
                current = boundary["slug"]
                if current in topics:
                    raise ValueError(f"Repeated promoted section slug: {current}")
                topics[current] = {"slug": current, "title": boundary["title"], "description": ""}
                seen.append(entry["tag"])
                promoted.add(entry["tag"])
            entry["topic"] = current
        if seen != list(boundaries):
            raise ValueError(f"Missing or reordered section boundaries: {original}")
        for chapter in configuration["chapters"]:
            if original in chapter["topics"]:
                position = chapter["topics"].index(original) + 1
                chapter["topics"][position:position] = [item["slug"] for item in promotions]
    # A canonical statement can move across source sections. Its embedded
    # descendants (including equations inside absorbed clauses) move with it.
    owners = {}
    for entry in entries.values():
        for variant in entry['variants'] + entry.get('components', []):
            for label in [variant['label'], *variant.get('aliases', [])]:
                owners[variant['source'], label] = entry['tag']
    parents = {}
    for tag, entry in entries.items():
        if entry['variants'][0].get('section'):
            continue
        candidates = set()
        for variant in entry['variants']:
            parent = owners.get((variant['source'], variant.get('parent_label')))
            if parent and parent != tag and not entries[parent]['variants'][0].get('section'):
                candidates.add(parent)
        if len(candidates) > 1:
            raise ValueError(f'Conflicting canonical parents: {tag}')
        if candidates:
            parents[tag] = candidates.pop()
    placed, active = {}, set()

    def place(tag):
        if tag in active:
            raise ValueError(f'Circular canonical parent: {tag}')
        if tag in placed:
            return
        active.add(tag)
        if tag in parents:
            place(parents[tag])
            entries[tag]['topic'] = entries[parents[tag]]['topic']
        active.remove(tag)
        placed[tag] = entries[tag]

    for tag in entries:
        place(tag)
    entries.clear()
    entries.update(placed)
    for entry in entries.values():
        variant = entry["variants"][0]
        entry["section_intro"] = bool(variant.get("section") and (entry["tag"] in promoted or title_key(variant["caption"]) == title_key(topics[entry["topic"]]["title"])))
    return configuration
