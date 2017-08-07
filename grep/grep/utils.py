import re
import os

def convert_patterns(patterns):
  results = []
  for pattern in patterns:
    results.append(re.compile(pattern))
  return results

def traverse_directories(top_directory):
  #print "top_directory {}".format(top_directory)
  results = []
  for root, directory, files in os.walk(top_directory):
    for file in files:
      #print os.path.join(root, file)
      results.append(os.path.join(root, file))
  return results

def apply_patterns(files, patterns):
  for file in files:
    # open file and read the lines
    #print file
    lines = open(file).readlines()
    search_in_lines(file, lines, patterns)


def search_in_lines(file, lines, patterns):
  #for each pattern:
  for num, line in enumerate(lines):
    #print num, line
    for pattern in patterns:
      if pattern.search(line):
          print "{}:{}: {}".format(
                        os.path.join(file),
                        num+1,
                        line)
