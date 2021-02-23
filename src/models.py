import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

"""class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}"""



class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), ForeignKey('favoritos.personaje_name'))
    gender = Column(String(250))
    hair_color = Column(String(250))
    birth_year = Column(String(250))
    height = Column(Integer)
    mass = Column(Integer)


class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    name = Column(String(250) ,ForeignKey('favoritos.planeta_name'))
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String(250))
    population = Column(Integer)
    climate = Column(String(250))    


class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), ForeignKey('favoritos.usuario_name'))
    genero = Column(String(250))
    correo = Column(String(250))
    telefono = Column(String(250))
    password = Column(String(250))


class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    personaje_name = (Integer, ForeignKey('personaje.name'))
    planeta_name = (Integer, ForeignKey('planeta.name'))
    usuario_name = (Integer, ForeignKey('usuario.name'))
      
    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')


""""""""""""""""
fav
id - personaje_id - planeta-id - usuario_id
1  -     anakin       -   null     -  AnoukRimola
2  -     r2-d2        -  null      -  123123123
3       null          gatito           123123123


"""""""""""""""""