from marshmallow import Schema, fields


class GroupSchema(Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "name", "status")
        ordered = True
