#!/usr/bin/python3
""" holds class User"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, Text
from hashlib import md5


class Users(BaseModel, Base):
    __tablename__ = 'users'
    name = Column(String(100), nullable=False)
    lastname = Column(String(150), nullable=False)
    email = Column(String(200), nullable=False)
    address = Column(Text)
    reference_address = Column(Text)
    phone_number = Column(String(20))
