from marshmallow import Schema, fields
from application.private.category.schemas.category import CategorySchema


class ProductSchema(Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "name", "status", "price", "category", "likes")
        ordered = True

    category = fields.Nested(CategorySchema)
