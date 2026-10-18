import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import vm from 'node:vm';

const code = readFileSync(new URL('../site/assets/redirect.js', import.meta.url), 'utf8');
function redirected(hash, fragments = {}, routes = {}) {
  let result;
  vm.runInNewContext(code, {
    URL,
    document: {documentElement: {dataset: {redirect: '../../sections/default/', fragments: JSON.stringify(fragments), fragmentRoutes: JSON.stringify(routes)}}},
    location: {href: `https://example.test/sections/old/${hash}`, hash, replace: value => {result = value;}},
  });
  return result;
}
test('legacy fragments retain their destination anchor', () => {
  assert.equal(redirected('#old', {old: 'new'}), 'https://example.test/sections/default/#new');
});
test('a historical heading can move to another section', () => {
  assert.equal(redirected('#entry-old', {}, {'entry-old': '../../sections/reorganized/#entry-new'}), 'https://example.test/sections/reorganized/#entry-new');
  assert.equal(redirected('#unknown'), 'https://example.test/sections/default/');
});
