from app.extensions import ma


# User Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'avatar_url', 'password_hash', 'created_on', 'updated_on')


# Chat Schema
class ChatSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_first', 'user_second', 'created_on', 'updated_on')


# Message Schema
class MessageSchema(ma.Schema):
    class Meta:
        fields = ('id', 'sender_id', 'chat_id', 'text', 'created_on', 'updated_on')


# Init User Schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Init Chat Schema
chat_schema = ChatSchema()
chats_schema = ChatSchema(many=True)

# Init Message Schema
message_schema = MessageSchema()
messages_schema = MessageSchema(many=True)
