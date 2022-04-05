from application.common.base import BaseModel
from extensions import db


class ProductLike(db.Model, BaseModel):
    __tablename__ = "product_like"

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))

    def create_object(self, dict_body):
        self.user_id = dict_body.get("user_id", self.user_id)
        self.product_id = dict_body.get("product_id", self.product_id)

        return self
