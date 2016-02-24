import requests
from bs4 import BeautifulSoup
from django.conf import settings


def get_parsel_status(barcode):
    assert barcode
    params = {
        'guid': settings.UKRPOSHTA_API_TOKEN,
        'culture': 'uk',
        'barcode': barcode
    }
    _resp = requests.get(settings.UKRPOSHTA_API_URL, params=params)
    assert _resp.status_code == 200
    soup = BeautifulSoup(_resp.content, 'xml')
    result = {
        'eventdescription': soup.find('eventdescription').text,
        'lastofficeindex': soup.find('lastofficeindex').text,
        'lastoffice': soup.find('lastoffice').text,
        'barcode': soup.find('barcode').text,
        'code': soup.find('code').text
    }
    return result
