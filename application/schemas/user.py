from marshmallow import Schema, fields


class UserInputSchema(Schema):
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


class UserOutputSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    email = fields.String()
    username = fields.String()
    document = fields.String()
    phone_number = fields.String()
    status = fields.Integer()

    class Meta:
        strict = True
        ordered = True
