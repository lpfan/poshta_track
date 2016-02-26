from django.core.urlresolvers import reverse

from api import serializers
from api.tests import ApiTestCase, factories


class TestPackageStatus(ApiTestCase):

    def _get_parsel_status(self, parsel_number):
        return self.client.get(reverse('parsel-status-detail', args=[parsel_number]))

    def test_get_parsel_status(self):
        resp = self._get_parsel_status('RO307757915EE')
        self.assertSuccess(resp)


class TestPackageViewSet(ApiTestCase):

    def _get_packages(self):
        return self.client.get(reverse('package-list'))

    def test_get_packages(self):
        package = factories.PackageFactory()

        resp = self._get_packages()
        self.assertSuccess(resp, expected_data=serializers.PackageSerializer(package).data)
