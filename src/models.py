import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)



class UserFavorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    favorited = Column(String(25))
    itsUser = relationship(User)
    user_id = Column(Integer, ForeignKey('User.id'))

class Character(Base):
    __tablename__ = 'Character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    Planet_Name = Column(String(250))
    Character = relationship(Character)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
