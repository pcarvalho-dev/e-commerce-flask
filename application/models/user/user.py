from passlib.handlers.pbkdf2 import pbkdf2_sha256

from extensions import db, BaseModel


class User(db.Model, BaseModel):
    __tablename__ = "user"

    name = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    document = db.Column(db.String(256))
    phone_number = db.Column(db.String(256))
    status = db.Column(db.Boolean, default=1)

    # ForeignKeys
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"))

    group = db.relationship('Group', backref='user', lazy=True, uselist=False)

    def set_password(self, password):
        self.password = pbkdf2_sha256.hash(password)[20:]

    def check_password(self, candidate):
        return pbkdf2_sha256.verify(candidate, f"$pbkdf2-sha256$29000{self.password}")

    def create_item(self, dict_body):
        self.name = dict_body.get("name", self.name)
        self.email = dict_body.get("email", self.email)
        self.set_password(dict_body["password"])
        self.document = dict_body.get("document", self.document)
        self.phone_number = dict_body.get("phone_number", self.phone_number)
        self.group_id = dict_body.get("group_id", 1)

        return self
