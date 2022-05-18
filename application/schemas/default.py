from marshmallow import Schema, fields


def default_schema(schema, many=False):
    class DefaultReturnSchema(Schema):
        status = fields.String()
        msg = fields.String()
        pagination = fields.Dict()
        summary = fields.Dict()
        data = fields.Nested(schema, many=many)

        class Meta:
            strict = True
            ordered = True

    return DefaultReturnSchema


class ImageSchema(Schema):
    class Meta:
        # Fields to expose
        fields = ("original", "small", "medium", "large")
        ordered = True
