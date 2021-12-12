from marshmallow import Schema


class GroupSchema(Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "name", "status")
        ordered = True
