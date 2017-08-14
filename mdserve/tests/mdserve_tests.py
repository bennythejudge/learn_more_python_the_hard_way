import os
from mdserve import blog
import unittest
import tempfile
from nose.tools import *
import uuid

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        blog.app.testing = True
        self.app = blog.app.test_client()

    def test_index(self):
      page = self.app.get('/')
      assert_true('Welcome to my blog' in page.data)
      assert_false('Welcome to my pippo' in page.data)

    def test_mdfile(self):
      page = self.app.get('/page1.html')
      assert_true('more stuff', page.data)

    def test_edit(self):
      token = uuid.uuid4().hex  
      print token
      page = self.app.get('/edit/page1.html')
      assert_true('Editing page1.md', page.data)
      page = self.app.post(
              '/edit/page1.html',
              data={'contents': token},
              follow_redirects=True)
      assert_true(token in page.data)

if __name__ == '__main__':
    unittest.main()
