from nose.tools import *
from mdgen import utils
import os
  
def test_traverse_directories():
  results = utils.traverse_directories('.')
  # assert we have the same contents (con chi?)
  assert_true('./mdgen/__init__.py' in results)

def test_discovery_targets():
  files = utils.traverse_directories('docs')
  results = utils.discover_md_files('docs', 'html', files)
  print results
  expecting = [('docs/index.md', 'html/index.html'), ('docs/page1.md', 'html/page1.html'), ('docs/test.md', 'html/test.html'), ('docs/level1/file1.md', 'html/level1/file1.html'), ('docs/level1/level11/file1.md', 'html/level1/level11/file1.html'), ('docs/level1/level11/level111/file1.md', 'html/level1/level11/level111/file1.html')]
  assert_equal(results, expecting)

def test_generate_html():
  source = 'docs/index.md'
  target = 'html/index.html'
  if os.path.exists(target):
    os.unlink(target)
  utils.convert_md_to_html(source, target)
  assert_true(os.path.exists(target))

def test_convert_md_directory():
  pass
