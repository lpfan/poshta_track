from datetime import datetime

from django.core.urlresolvers import reverse

from api import serializers, models
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

    def _get_package(self, barcode):
        return self.client.get(reverse('package-detail', args=[barcode]))

    def _create_package(self, barcode=None, eventdescription=None, lastofficeindex=None,
                        lastoffice=None, code=None, created=None, updated=None, client_id=None):
        data = {}
        if barcode is not None:
            data['barcode'] = barcode
        if eventdescription is not None:
            data['eventdescription'] = eventdescription
        if lastofficeindex is not None:
            data['lastofficeindex'] = lastofficeindex
        if lastoffice is not None:
            data['lastoffice'] = lastoffice
        if code is not None:
            data['code'] = code
        if created is not None:
            data['created'] = created
        if updated is not None:
            data['updated'] = updated
        if client_id is not None:
            data['client_id'] = client_id

        return self.client.post(reverse('package-list'), data=data)

    def _update_package(self, package_barcode, barcode=None, eventdescription=None, lastofficeindex=None,
                        lastoffice=None, code=None, created=None, updated=None, client_id=None):
        data = {}
        if barcode is not None:
            data['barcode'] = barcode
        if eventdescription is not None:
            data['eventdescription'] = eventdescription
        if lastofficeindex is not None:
            data['lastofficeindex'] = lastofficeindex
        if lastoffice is not None:
            data['lastoffice'] = lastoffice
        if code is not None:
            data['code'] = code
        if created is not None:
            data['created'] = created
        if updated is not None:
            data['updated'] = updated
        if client_id is not None:
            data['client_id'] = client_id

        return self.client.put(reverse('package-detail', args=[package_barcode]), data=data)

    def test_get_package(self):
        package = factories.PackageFactory(created=datetime.now())

        resp = self._get_package(package.barcode)
        self.assertSuccess(resp, expected_data=serializers.PackageSerializer(package.reload()).data)

    def test_get_packages(self):
        package1 = factories.PackageFactory()
        package2 = factories.PackageFactory()

        resp = self._get_packages()
        self.assertObjectsInResponse(resp, [package1, package2], serializers.PackageSerializer)

    def test_create_package(self):
        response = self._create_package(
            barcode=factories._generate_random_string(),
            eventdescription=factories._generate_random_string(),
            lastoffice='post',
            lastofficeindex='0211',
            code='0000'
        )
        self.assertObjectCreated(
            response,
            models.Package,
            serializers.PackageSerializer
        )
