from django.core.urlresolvers import reverse

from api import serializers
from api.tests import ApiTestCase, MongoTestCase, factories


class TestPackageStatus(ApiTestCase):

    def _get_parsel_status(self, parsel_number):
        return self.client.get(reverse('parsel-status-detail', args=[parsel_number]))

    def test_get_parsel_status(self):
        resp = self._get_parsel_status('RO307757915EE')
        self.assertSuccess(resp)


class TestPackageViewSet(MongoTestCase, ApiTestCase):

    def _get_packages(self):
        return self.client.get(reverse('package-list'))

    def _get_package(self, barcode):
        return self.client.get(reverse('package-detail', args=[barcode]))

    def test_get_package(self):
        package = factories.PackageFactory()

        resp = self._get_package(package.barcode)
        self.assertSuccess(resp, expected_data=serializers.PackageSerializer(package).data)

    def test_get_packages(self):
        package1 = factories.PackageFactory()
        package2 = factories.PackageFactory()
        import ipdb; ipdb.set_trace()

        resp = self._get_packages()
        self.assertObjectsInResponse(resp, [package1, package2], serializers.PackageSerializer)
