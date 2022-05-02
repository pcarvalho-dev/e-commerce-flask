from apiflask import Schema, fields


class UserSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.String()
    status = fields.Integer()

    class Meta:
        strict = True
        ordered = True
