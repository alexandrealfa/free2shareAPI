from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    nickname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=True)
    phone = db.Column(db.String, nullable=False)
    link_profile_picture = db.Column(db.String, nullable=False)
    bio = db.Column(db.Text, nullable=False)

    favorites_list = db.relationship("FavoriteModel", backref=db.backref("favorite_list", lazy="joined"), lazy="joined")

    @property
    def password(self):
        raise TypeError("A senha não pode ser acessada")

    @password.setter
    def password(self, new_password):
        new_password_hash = generate_password_hash(new_password)
        self.password_hash = new_password_hash

    def check_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)
