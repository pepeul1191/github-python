## GitHub Python

Requisitos de software previamente instalado:

+ Python 3.5
+ Python PIP

### Descipción

En caso de usar el servicio en python:

    $ sudo pip install virtualenv
    $ virtualenv -p python3 <<nombre_ambiente>>
    $ cd <<nombre_ambiente>>
    $ source bin/activate

Arrancar aplicación con servidor Werkzeug:

    $ cd <<carpeta-proyecto>>
    $ pip install -r requirements.txt
    $ python app.py

Dejar de seguir versionando archivo pero sin eliminar:

    $ git update-index --assume-unchanged client.py


### PyLint

    $ pylint <archivo>.py --reports=yes
    $ pylint **/*.py --reports=yes

---

Fuentes:

+ https://www.pylint.org/#install
+ https://websemantics.uk/articles/displaying-code-in-web-pages/
+ https://pygithub.readthedocs.io/en/latest/introduction.html
+ https://bottlepy.org/docs/dev/
+ https://cdnjs.com/libraries/github-markdown-css
+ https://github.com/sindresorhus/github-markdown-css
+ https://cdnjs.com/libraries/SyntaxHighlighter
+ https://o7planning.org/en/10375/highlighting-code-with-syntaxhighlighter-javascript-library
