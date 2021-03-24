import json
import random

from tests.unit import test_first, test_string


class TestUser:

    def test_create_chat(self, test_app):
        with test_app.test_client() as client:
            test_user_first = client.post('/users/create', json=json.loads(json.dumps({u'name': test_string,
                                                                                       u'email': test_string,
                                                                                       u'password': test_string}
                                                                                      ))).json['id']
            test_user_second = client.post('/users/create', json=json.loads(json.dumps({u'name': test_string,
                                                                                        u'email': test_string + str(
                                                                                            random.choice(
                                                                                                [i for i in
                                                                                                 range(1000)])),
                                                                                        u'password': test_string}
                                                                                       ))).json['id']
            test_chat = client.post('/chats/create', json=json.loads(json.dumps({u'user_first': test_user_first,
                                                                                 u'user_second': test_user_second}
                                                                                ))).json['id']
            response = client.post('/messages/create', json=json.loads(json.dumps({u'sender_id': test_user_first,
                                                                                   u'chat_id': test_chat,
                                                                                   u'text': test_string})))
            assert response.status_code == 200

    def test_get_chat(self, test_app):
        with test_app.test_client() as client:
            response = client.get('/messages/%s' % test_first)
            assert response.status_code == 200

    def test_get_chats(self, test_app):
        with test_app.test_client() as client:
            response = client.get('/messages/%s/all' % test_first)
            assert response.status_code == 200

    def test_delete_message(self, test_app):
        with test_app.test_client() as client:
            response = client.delete('/messages/%s' % test_first)
            assert response.status_code == 200

            client.delete('/chats/%s' % test_first)

            test_user_first = client.get('/users').json[-1]['id']
            client.delete('/users/%s' % test_user_first)
            test_user_second = client.get('/users').json[-1]['id']
            client.delete('/users/%s' % test_user_second)
