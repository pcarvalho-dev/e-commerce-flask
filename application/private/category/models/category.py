import uuid

from application.common.base import BaseModel
from extensions import db


class Category(db.Model, BaseModel):
    __tablename__ = "category"

    hash_id = db.Column(db.String(36), unique=True, nullable=False)
    name = db.Column(db.String(256), nullable=False)
    status = db.Column(db.Boolean, default=1)
    slug = db.Column(db.String(256))
    description = db.Column(db.String(256))

    def create_object(self, dict_body):
        self.hash_id = str(uuid.uuid4())
        self.name = dict_body.get("name", self.name)
        self.status = dict_body.get("status", self.status)
        self.slug = dict_body.get("slug", self.slug)
        self.description = dict_body.get("description", self.description)

        return self
