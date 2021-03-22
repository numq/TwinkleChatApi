from sqlalchemy import Column, Integer, Text, func, String
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
    password_hash = Column(String(128))

    def __repr__(self) -> str:
        return f"User({self.id}, {self.name}, {self.email}, {self.created_on})"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
