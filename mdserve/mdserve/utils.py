import os
import markdown

def convert_md_to_html(doc):
    content = open(doc).read()
    html = markdown.markdown(content)
    return html
