from http import HTTPStatus

from django.conf import settings
from django.test import TestCase


class MongoTestCase(TestCase):
    test_db = 'test_{}'.format(settings.MONGO_DATABASE_NAME)

    def _pre_setup(self):
        from mongoengine.connection import connect, disconnect
        disconnect()
        connect(self.test_db, port=settings.MONGO_PORT)
        super(MongoTestCase, self)._pre_setup()

    def _post_teardown(self):
        from mongoengine.connection import get_connection, disconnect
        connection = get_connection()
        connection.drop_database(self.test_db)
        disconnect()
        super(MongoTestCase, self)._post_teardown()


class ApiTestCase(TestCase):

    def assertSuccess(self, response, expected_data=None):
        if response.status_code not in (HTTPStatus.OK, HTTPStatus.CREATED, HTTPStatus.ACCEPTED, HTTPStatus.NO_CONTENT):
            if hasattr(response, 'data'):
                self.fail('Response error (%s): %s' % (response.status_code, response.data))
        if expected_data:
            self.assertEqual(response.data, expected_data)

    def assertObjectsInResponse(self, response, expected_objects, serializer):
        self.assertSuccess(response)
        expected_data = serializer(expected_objects, many=True).data
        self.assertEqual(response.data, expected_data)
