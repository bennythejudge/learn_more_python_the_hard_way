from nose.tools import *
from mdgen import utils
  
def test_traverse_directories():
  results = utils.traverse_directories('.')
  # assert we have the same contents (con chi?)
  assert_true('./mdgen/__init__.py' in results)
