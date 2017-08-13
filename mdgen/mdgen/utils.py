import os
import re
import markdown

def traverse_directories(top_directory):
  #print "top_directory {}".format(top_directory)
  results = []
  for root, directory, files in os.walk(top_directory):
    for file in files:
      #print os.path.join(root, file)
      results.append(os.path.join(root, file))
  return results

def discover_md_files(source, target, files):
    results = []
    # get an expression for .*.md"
    expr = re.compile('.*.md$')
    for file in files:
      filename = os.path.basename(file)
      if expr.match(filename):
          print "------"
          # print file
          print "filename {}".format(filename)
          # extract the directoy below the top level (which is = source)
          directory = os.path.split(file)[0][len(source)+1:]
          # print "directory: {}".format(directory)
          target_dir = os.path.join(target, directory)
          # print "target_dir {}".format(target_dir)
          if not os.path.exists(target_dir):
              # print "making dir {}".format(target_dir)
              os.makedirs(target_dir)
          # make filename
          base, ext = os.path.splitext(filename)
          # print base, ext
          target_file = os.path.join(target_dir, base + '.html')
          results.append((file, target_file))
    return results

def convert_md_to_html(source, target):
    lines = open(source).read()
    # print "lines: {}\n".format(lines)
    html = markdown.markdown(lines)
    # print "html: {}\n".format(html)
    print "writing to {}".format(target)
    with open(target, 'w') as f:
        f.write(html)
