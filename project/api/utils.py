import requests
from bs4 import BeautifulSoup


def get_parsel_status_html(parsel_code):
    assert parsel_code
    url = "http://services.ukrposhta.ua/bardcodesingle/\
           DownloadInfo.aspx?id={}".format(parsel_code)
    _resp = requests.get(url)
    soup = BeautifulSoup(_resp.content, 'html.parser')
    soup.find(id="container")
    return soup.get_text()
