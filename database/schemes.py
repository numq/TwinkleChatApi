from flask_marshmallow import Marshmallow

from main import app

# Init ma
ma = Marshmallow(app)


# User Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'password_hash', 'created_on', 'updated_on')


# Init user schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)
