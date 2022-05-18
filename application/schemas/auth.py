from marshmallow import Schema, fields

class AuthInputSchema(Schema):
    username = fields.String()
    password = fields.String()
    grant_type = fields.String()

    class Meta:
        strict = True
        ordered = True
