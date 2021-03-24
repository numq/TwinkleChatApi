import datetime


def datetime_format(value):
    return datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')


def is_exists(db, model, arg):
    return db.session.query(model).get(arg) is not None
