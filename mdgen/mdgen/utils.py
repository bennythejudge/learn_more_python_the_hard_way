import os

def traverse_directories(top_directory):
  #print "top_directory {}".format(top_directory)
  results = []
  for root, directory, files in os.walk(top_directory):
    for file in files:
      #print os.path.join(root, file)
      results.append(os.path.join(root, file))
  return results
