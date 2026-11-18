# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import Flask
from flask_cors import CORS

from api.routes import rest_api
from api.models import db

# Create App
app = Flask(__name__)

# load Config 
app.config.from_object('api.config.BaseConfig')

# Connect Flask and SqlAlchemy
db.init_app(app)

# Connect Flask and FlaskRestX
rest_api.init_app(app)

# Enable CORS
CORS(app)

# Flask 2.3 removed before_first_request. Create the tables as soon as the
# app is imported so `python run.py` and gunicorn both start ready to serve.
with app.app_context():
    db.create_all()
