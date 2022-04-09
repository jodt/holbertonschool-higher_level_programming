#!/usr/bin/python3
"""
This is the model_state module
that contains the class definition of a State
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    This is the class State
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128),  nullable=False)
