from flask import request
from sqlalchemy import or_

from app.blueprints import bp_chat
from app.extensions import db
from app.utilities import exceptions
from database import models
from database.schemes import chats_schema, chat_schema


# Create Chat
@bp_chat.route('/chats/create', methods=['POST'])
def create_chat():
    new_chat = models.Chat()
    users = sorted([request.json["user_first"], request.json["user_second"]])
    new_chat.user_first = users[0]
    new_chat.user_second = users[1]

    if db.session.query(models.Chat).filter_by(id=new_chat.id).count() < 1 and models.Chat.query.filter_by(
            user_first=new_chat.user_first, user_second=new_chat.user_second).count() < 1:
        db.session.add(new_chat)
        db.session.commit()
        return chat_schema.jsonify(new_chat)
    else:
        return exceptions.DbEntryExists[0], exceptions.DbEntryExists[1]


# Get Single Chat
@bp_chat.route('/chats/<id>', methods=['GET'])
def get_chat(id=None):
    chat = models.Chat.query.get(id)
    return chat_schema.jsonify(chat)


# Get All Chats
@bp_chat.route('/chats/<user_id>/all', methods=['GET'])
def get_chats(user_id=None):
    all_chats = models.Chat.query.filter(or_(
        models.Chat.user_first.like(user_id), models.Chat.user_second.like(user_id))).all()
    result = chats_schema.jsonify(all_chats)
    return result


# Delete Chat
@bp_chat.route('/chats/<id>', methods=['DELETE'])
def delete_chat(id=None):
    chat = models.Chat.query.get(id)
    db.session.delete(chat)
    db.session.commit()
    return chat_schema.jsonify(chat)
