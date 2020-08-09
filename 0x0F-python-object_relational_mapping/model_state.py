#!/usr/bin/python3
"""
a python file that contains the class definition of a State
and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(BASE):
    """a class to create a table in a db"""

    __tablename__ = 'states'
    id = Column(Integer, UNIQUE, AUTO GENERATED, NOT NULL, primary_key=True)
    name = Column(String(128), NOT NULL)
