from django.test import TestCase


class ApiTestCase(TestCase):

    def assertSuccess(self, response):
        self.assertEqual(response.status_code, 200)
