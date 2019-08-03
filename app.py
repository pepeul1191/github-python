#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, template
from markdown2 import Markdown
from client import g

def list_content(repo_url):
    repo = g.get_repo(repo_url)
    contents = repo.get_contents('')
    while contents:
        file_content = contents.pop(0)
        if file_content.type == 'dir':
            contents.extend(repo.get_contents(file_content.path))
        else:
            print(file_content)

def get_content(repo_url, path, file):
    repo = g.get_repo(repo_url)
    return repo.get_contents(path + file)

# list_content('pepeul1191/flask-boilerplate-v3')

@route('/demo')
def demo():
    file_content = get_content('pepeul1191/flask-boilerplate-v3', '/main/', 'middlewares.py')
    code = str(file_content.decoded_content, 'utf-8')
    return template('view_py', code=code)

@route('/readme')
def demo():
    file_content = get_content('pepeul1191/flask-boilerplate-v3', '', 'README.md')
    markdowner = Markdown()
    html = markdowner.convert(str(file_content.decoded_content, 'utf-8'))
    return template('readme', html=html)


run(host='localhost', port=8082, debug=True)
