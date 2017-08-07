from nose.tools import *
from grep import utils
import re

def test_convert_patterns():
  results = utils.convert_patterns(['.*.py'])
  assert_equal(results, [re.compile('.*.py')])

def test_traverse_directories():
  results = utils.traverse_directories('.')
  # assert we have the same contents (con chi?)
  print results
  assert_true('./grep/__init__.py' in results)

def test_apply_patterns():
  files = utils.traverse_directories('.')
  patterns = utils.convert_patterns(['.*.py'])
  utils.apply_patterns(files, patterns)
  # assert
