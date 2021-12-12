from passlib.handlers.pbkdf2 import pbkdf2_sha256

from application.models.base import BaseModel
from extensions import db


class Group(db.Model, BaseModel):
    __tablename__ = "group"

    name = db.Column(db.String(256), nullable=False)
    status = db.Column(db.Boolean, default=1)

    def create_object(self, dict_body):
        self.name = dict_body.get("name", self.name)
        self.status = dict_body.get("status", self.status)

        return self
