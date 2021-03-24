from flask import request

from app.blueprints import bp_message
from app.extensions import db
from app.utilities import exceptions
from database import models
from database.schemes import message_schema, messages_schema


# Create Message
@bp_message.route('/messages/create', methods=['POST'])
def create_message():
    new_message = models.Message()
    new_message.sender_id = request.json['sender_id']
    new_message.chat_id = request.json['chat_id']
    new_message.text = request.json['text']

    if db.session.query(models.Message).filter_by(id=new_message.id).count() < 1:
        db.session.add(new_message)
        db.session.commit()
        return message_schema.jsonify(new_message)
    else:
        return exceptions.DbEntryExists[0], exceptions.DbEntryExists[1]


# Get Single Message
@bp_message.route('/messages/<id>', methods=['GET'])
def get_message(id=None):
    message = models.Message.query.get(id)
    return message_schema.jsonify(message)


# Get All Messages
@bp_message.route('/messages/<chat_id>/all', methods=['GET'])
def get_messages(chat_id=None):
    all_messages = models.Message.query.filter_by(chat_id=chat_id).all()
    result = messages_schema.jsonify(all_messages)
    return result


# Delete Message
@bp_message.route('/messages/<id>', methods=['DELETE'])
def delete_message(id=None):
    message = models.Message.query.get(id)
    db.session.delete(message)
    db.session.commit()
    return message_schema.jsonify(message)
