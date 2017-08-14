import markdown
from flask import Flask
from mdserve import utils
import os
from flask import render_template
from flask import request
from flask import redirect

app = Flask(__name__)

# on / serve index.md
@app.route("/")
def index():
    # convert to html
    filename = os.path.join('docs', 'index.md')
    html = utils.convert_md_to_html(filename)
    return render_template('layout.html', body=html, doc='index')

@app.route('/<doc>.html')
def mdfile(doc):
    filename = os.path.join('docs', doc + '.md')
    html = utils.convert_md_to_html(filename)
    return render_template('layout.html', body=html, doc=doc)

@app.route("/<subdir>/<doc>.html")
def subdirs(subdir, doc):
    print "subdir: {} doc {}".format(subdir, doc)
    filename = os.path.join('docs', subdir, doc + '.md')
    print "filename: {}".format(filename)
    html = utils.convert_md_to_html(filename)
    return render_template("subdir_template.html", body=html)

@app.route("/edit/<doc>.html", methods=['POST', 'GET'])
def edit(doc):
    if request.method == 'POST':
        contents = request.form['contents']
        mdfile = os.path.join("docs", doc + ".md")
        print mdfile
        with open(mdfile, 'w') as f:
            f.write(contents)
        return redirect(doc + '.html')
    else:
        contents = open(os.path.join("docs", doc + ".md")).read()
        return render_template('edit.html', doc=doc, contents=contents)
