#!/usr/bin/env python
import os
from mdgen import utils

source_directory = 'docs'

# estrai directory vs file

files = utils.traverse_directories(source_directory)
print files


path = 'docs/dir1/dir11/dir111'

print os.path.basename(path)
print os.path.abspath(path)
print os.path.dirname(path)
print os.path.split(path)
print os.path.splitext(path)

