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
