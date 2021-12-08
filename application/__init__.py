from flask import Flask

from application.services.date_and_time import get_now
from config import Config
from extensions import cors, jwt, db, ma


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI

    # Extensions
    cors.init_app(app, resources={r"/*": {"origins": "*"}})
    jwt.init_app(app)
    db.init_app(app)
    ma.init_app(app)

    from application.routes import tests
    tests.init_app(app)

    return app


class BaseModel(db.Model):
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    created_at = db.Column(db.DateTime, default=get_now)
    updated_at = db.Column(db.DateTime, default=get_now, onupdate=get_now)
    deleted_at = db.Column(db.DateTime)

    @classmethod
    def get_by_id(cls, record_id):
        return cls.query.get(int(record_id))
