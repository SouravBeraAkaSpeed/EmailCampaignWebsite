import urllib
import requests

API_KEY = ""


def generate(url):
    url = url
    CUSTOM_URL_ALIAS = ""
    key = API_KEY
    url = urllib.parse.quote(url)
    name = CUSTOM_URL_ALIAS
    r = requests.get(
        'http://cutt.ly/api/api.php?key={}&short={}&name={}'.format(key, url, name)).json()['url']['shortLink']
    return r
