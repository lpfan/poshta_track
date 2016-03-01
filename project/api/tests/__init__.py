import ujson
from http import HTTPStatus

from django.conf import settings
from django.test import TestCase, Client


def _dump_data(data, content_type):
    if content_type == 'application/json':
        return data and ujson.dumps(data)
    raise Exception('Unexpected content type: {}'.format(content_type))


class ApiClient(Client):

    def post(self, path, data=None, content_type='application/json', **extra):
        data = _dump_data(data, content_type)
        return super(ApiClient, self).post(path, data=data, content_type=content_type, **extra)

    def put(self, path, data='', content_type='application/json', **extra):
        data = _dump_data(data, content_type)
        return super(ApiClient, self).put(path, data=data, content_type=content_type, **extra)

    def patch(self, path, data='', content_type='application/json', **extra):
        data = _dump_data(data, content_type)
        return super(ApiClient, self).patch(path, data=data, content_type=content_type, **extra)


class ApiTestCase(TestCase):
    client_class = ApiClient
    test_db = 'test_{}'.format(settings.MONGO_DATABASE_NAME)

    def _pre_setup(self):
        from mongoengine.connection import connect, disconnect
        disconnect()
        connect(self.test_db, port=settings.MONGO_PORT)
        super(ApiTestCase, self)._pre_setup()

    def _post_teardown(self):
        from mongoengine.connection import get_connection, disconnect
        connection = get_connection()
        connection.drop_database(self.test_db)
        disconnect()
        super(ApiTestCase, self)._post_teardown()

    def assertSuccess(self, response, expected_data=None):
        if response.status_code not in (HTTPStatus.OK, HTTPStatus.CREATED, HTTPStatus.ACCEPTED, HTTPStatus.NO_CONTENT):
            if hasattr(response, 'data'):
                self.fail('Response error (%s): %s' % (response.status_code, response.data))
        if expected_data:
            self.assertAlmostEqual(response.data, expected_data)

    def assertObjectsInResponse(self, response, expected_objects, serializer):
        self.assertSuccess(response)
        expected_objects = [o.reload() for o in expected_objects]
        expected_data = serializer(expected_objects, many=True).data
        self.assertEqual(response.data, expected_data)

    def assertObjectCreated(self, response, model, serializer):
        self.assertSuccess(response)
        instance = model.objects.get(barcode=response.data['barcode'])
        # self.assertAlmostEqual(response.data, serializer(instance).data)

    def assertObjectUpdated(self, response, instance, serializer):
        self.assertSuccess(response)
