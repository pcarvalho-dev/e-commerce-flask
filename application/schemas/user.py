from apiflask import Schema, fields


class UserInputSchema(Schema):
    name = fields.String()
    status = fields.Integer()

    class Meta:
        strict = True
        ordered = True


class UserOutputSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    status = fields.Integer()

    class Meta:
        strict = True
        ordered = True
