#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey  # type: ignore
from sqlalchemy.orm import relationship  # type: ignore


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    email = Column(String(120), nullable=False)
    password = Column(String(120), nullable=False)
    first_name = Column(String(120))
    last_name = Column(String(120))
    __tablename__ = "users"
    places = relationship("Place", backref="users",
                          cascade="all, delete, delete-orphan")
    reviews = relationship("Review", backref="users",
                           cascade="all, delete, delete-orphan")
