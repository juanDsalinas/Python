from flask import Flask
from routes.contacts import contacts
# from utils.db import Base

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine


Base = declarative_base()

app = Flask(__name__)
app.register_blueprint(contacts)

cad_con = 'mysql://root:@localhost/api_flask'
engine = create_engine(cad_con)


@app.route('/')
def hello():
    return "Entro"


