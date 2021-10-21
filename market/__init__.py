from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///my_marketplace.db'
db = SQLAlchemy(app)

from market.admin import routes
