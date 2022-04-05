from application.common.base import BaseModel
from application.private.category.models.category import Category
from application.private.product.models.product_like import ProductLike
from extensions import db


class Product(db.Model, BaseModel):
    __tablename__ = "product"

    name = db.Column(db.String(256), nullable=False)
    status = db.Column(db.Boolean, default=1)
    price = db.Column(db.Float, default=0)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    category = db.relationship(Category, uselist=False, backref="product")

    def _get_likes(self):
        products = ProductLike.query.filter(
            ProductLike.product_id == self.id, ProductLike.deleted_at.is_(None)).count()
        return int(products)

    likes = property(_get_likes)

    def create_object(self, dict_body):
        self.name = dict_body.get("name", self.name)
        self.status = dict_body.get("status", self.status)
        self.price = dict_body.get("price", self.price)
        self.category_id = dict_body.get("category_id", self.category_id)

        return self
