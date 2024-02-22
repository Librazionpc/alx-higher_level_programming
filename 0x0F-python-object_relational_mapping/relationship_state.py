#!/usr/bin/python3
"""Linking a class to a table in the database
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class that links to the MySQL Table States"""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(126), nullable=False)
    cities = relationship("City", backref="states")
