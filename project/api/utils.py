import requests
from bs4 import BeautifulSoup
from rinse.message import SoapMessage
from rinse.client import SoapClient
from lxml import etree
from rinse.util import printxml


def get_parsel_via_soap(parsel_code):
    url = 'http://services.ukrposhta.com/barcodestatistic/barcodestatistic.asmx?WSDL'
    body = etree.Element('GetBarcodeInfo')
    guid = etree.SubElement(body, 'guid')
    guid.text = 'fcc8d9e1-b6f9-438f-9ac8-b67ab44391dd'
    culture = etree.SubElement(body, 'culture')
    culture.text = 'uk'
    barcode = etree.SubElement(body, 'barcode')
    barcode.text = parsel_code
    msg = SoapMessage(body)
    client = SoapClient(url, debug=True)
    resp = client(msg)


def get_parsel_status_html(parsel_code):
    assert parsel_code
    url = "http://services.ukrposhta.ua/bardcodesingle/\
           DownloadInfo.aspx?id={}".format(parsel_code)
    _resp = requests.get(url)
    soup = BeautifulSoup(_resp.content, 'html.parser')
    soup.find(id="container")
    return soup.get_text()
