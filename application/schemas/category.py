from marshmallow import Schema


class CategorySchema(Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "hash_id", "name", "status",
                  "slug", "description")
        ordered = True
