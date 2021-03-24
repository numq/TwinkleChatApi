import json
import random

from tests.unit import test_user_id, test_string


class TestUser:

    def test_create_user(self, test_app):
        with test_app.test_client() as client:
            response = client.post('/users/create', json=json.loads(json.dumps({u'name': test_string,
                                                                                u'email': test_string,
                                                                                u'password': test_string})))
            assert response.status_code == 200

    def test_get_user(self, test_app):
        with test_app.test_client() as client:
            test_id = client.get('/users').json[-1]['id']
            response = client.get('/users/%s' % test_id)
            assert response.status_code == 200

    def test_get_users(self, test_app):
        with test_app.test_client() as client:
            response = client.get('/users')
            assert response.status_code == 200

    def test_update_user(self, test_app):
        with test_app.test_client() as client:
            user_id = client.get('/users').json[-1]['id']
            response = client.put('/users/%s' % user_id, json=json.loads(json.dumps({u'id': test_user_id,
                                                                                     u'name': test_string,
                                                                                     u'email': test_string + str(
                                                                                         random.choice(
                                                                                             [i for i in range(1000)])),
                                                                                     u'password': test_string})))
            assert response.status_code == 200

    def test_delete_user(self, test_app):
        with test_app.test_client() as client:
            response = client.delete('/users/%s' % test_user_id)
            assert response.status_code == 200
