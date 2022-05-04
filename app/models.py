from datetime import datetime
from enum import unique
from xmlrpc.client import Boolean, boolean
from flask_appbuilder import Model
from flask import Markup
from app import db
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from flask_appbuilder.models.decorators import renders


class Contact(Model):
    id = Column(Integer, primary_key=True)
    pid = Column(Integer, unique = False, nullable=False)
    name =  Column(String(150), unique = False, nullable=False)
    address =  Column(String(564))
    expiration = Column(Date, nullable=False)
    entered = Column(Date, nullable=False)
    temporary = Column(db.Boolean, default=False, nullable=True)
    included = Column(db.Boolean, default=False, nullable=True)

    @renders('expiration')
    def flagged_expiration(self):
        if (self.expiration < datetime.now().date()):
            return Markup('<div style="color:red;"><b>' + str(self.expiration) + '</b></div>')
        else:
            return Markup(str(self.expiration))

    def __repr__(self):
        return self.name