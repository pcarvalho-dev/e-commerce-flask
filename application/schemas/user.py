from marshmallow import Schema, fields


class UserSchema(Schema):
    name = fields.String(required=True)
    email = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    document = fields.String(required=True)
    phone_number = fields.String()
    status = fields.Integer(allow_none=True)

    class Meta:
        strict = True
        ordered = True