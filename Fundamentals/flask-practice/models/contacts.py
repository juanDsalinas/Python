import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from app import Base

class Pais(Base):
    __tablename__ = 'país'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    continente = Column(String(20))
    habitantes = Column(Integer)
    moneda = Column(String(30))

    def __init__(self, nombre, continente, habitantes, moneda):
        self.nombre = nombre
        self.continente = continente
        self.habitantes = habitantes
        self.moneda = moneda

    def __repr__(self):
        return 'Pais' + (self.nombre)
