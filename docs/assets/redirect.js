const fragments = JSON.parse(document.documentElement.dataset.fragments || '{}');
const routes = JSON.parse(document.documentElement.dataset.fragmentRoutes || '{}');
const fragment = decodeURIComponent(location.hash.slice(1));
const destination = new URL(routes[fragment] || document.documentElement.dataset.redirect, location.href);
if (fragment && fragments[fragment]) destination.hash = fragments[fragment];
location.replace(destination.href);
