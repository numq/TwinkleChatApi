from app.extensions import ma


# User Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'password_hash', 'created_on', 'updated_on')


# Init User Schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)
