#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey  # type: ignore
from sqlalchemy.orm import relationship  # type: ignore


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
    __tablename__ = "cities"
    places = relationship("Place", backref="cities",
                          cascade="all, delete, delete-orphan")
