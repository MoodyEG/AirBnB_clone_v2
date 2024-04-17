#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, Float, ForeignKey  # type: ignore
from sqlalchemy import Integer, String, Table  # type: ignore
from sqlalchemy.orm import relationship  # type: ignore
from os import getenv


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60), ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(120), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    __tablename__ = "places"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="places",
                               cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """ Getter """
            from models import storage
            rev_list = []
            for rev in storage.all(Review).values():
                if rev.place_id == self.id:
                    rev_list.append(rev)
            return rev_list

        @property
        def amenities(self):
            """ Getter """
            from models import storage
            ami_list = []
            for ami in storage.all(Amenity).value():  # type: ignore
                if ami.place_id == self.id:
                    ami_list.append(ami)
            return ami_list

        @amenities.setter
        def amenities(self, obj=None):
            """ Setter """
            if obj:
                if obj.id not in self.amenity_ids\
                     and type(obj) == Amenity:  # type: ignore
                    self.amenity_ids.append(obj.id)
