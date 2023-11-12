#!/usr/bin/python3
""" defining User class """
from models.base_model import BaseModel


class User(BaseModel):
    """ User initialised """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
