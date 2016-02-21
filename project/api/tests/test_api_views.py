from django.core.urlresolvers import reverse

from api.tests import ApiTestCase


class TestParcelStatus(ApiTestCase):

    def _get_parsel_status(self, parsel_number):
        return self.client.get(reverse('parsel-status-detail', args=[parsel_number]))

    def test_get_parsel_status(self):
        resp = self._get_parsel_status('RO307757915EE')
        self.assertSuccess(resp)
