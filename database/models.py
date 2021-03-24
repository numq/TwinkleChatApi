from sqlalchemy import Column, Integer, Text, func, String, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions import db


class Base(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_on = Column(Text, default=func.now(), nullable=False)
    updated_on = Column(Text, default=func.now(), onupdate=func.now(), nullable=False)


class User(Base):
    __tablename__ = 'users'

    name = Column(String(20), nullable=True)
    email = Column(String(120), unique=True)
    avatar_url = Column(String(120), nullable=True)
    password_hash = Column(String(128))

    messages = db.relationship('Message', backref='user', lazy='dynamic')

    def __repr__(self) -> str:
        return f"User({self.id}, {self.name}, {self.email}, {self.created_on})"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Chat(Base):
    __tablename__ = 'chats'

    user_first = Column(Integer)
    user_second = Column(Integer)

    messages = db.relationship('Message', backref='chat', lazy='dynamic')

    def __repr__(self) -> str:
        return f"Chat({self.id}, {self.users}, {self.created_on})"


class Message(Base):
    __tablename__ = 'messages'

    sender_id = Column(Integer, ForeignKey('users.id'))
    chat_id = Column(Integer, ForeignKey('chats.id'))
    text = Column(String(240))

    def __repr__(self) -> str:
        return f"Message({self.id}, {self.sender_id}, {self.chat_id}, {self.text}, {self.created_on})"
