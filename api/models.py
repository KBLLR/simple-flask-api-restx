# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select

db = SQLAlchemy()

class Datas(db.Model):

    id           = db.Column(db.Integer()   , primary_key=True)
    data         = db.Column(db.String(256) , nullable=False)
    date_created = db.Column(db.DateTime()  , default=datetime.utcnow)

    def __repr__(self):
        return str( self.id ) 

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update_data(self, new_data):
        self.data = new_data

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        return db.session.get(cls, id)

    @classmethod
    def get_all(cls):
        return db.session.scalars(select(cls)).all()

    def toDICT(self):

        cls_dict         = {}
        cls_dict['_id']  = self.id
        cls_dict['data'] = self.data

        return cls_dict

    def toJSON(self):

        return self.toDICT()
