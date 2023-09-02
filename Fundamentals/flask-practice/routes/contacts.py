from flask import Blueprint,render_template

contacts = Blueprint('contacts',__name__)

@contacts.route('/contra')
def hello():
    return render_template("index.html")

@contacts.route('/new')
def new():
    return "Nuevo contacto"


@contacts.route('/update')
def update():
    return "update a contacto"


@contacts.route('/delete')
def delete():
    return "delete a contacto"
