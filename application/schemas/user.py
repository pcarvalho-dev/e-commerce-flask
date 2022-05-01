from marshmallow import Schema


class UserSchema(Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "name", "email", "phone_number", "status")
        ordered = True
