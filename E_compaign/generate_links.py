import urllib
import requests

API_KEY = ""


def generate(url):
    try:
        
        CUSTOM_URL_ALIAS = ""
        key = API_KEY
        url = urllib.parse.quote(url)
        name = CUSTOM_URL_ALIAS
        r = requests.get(
            'http://cutt.ly/api/api.php?key={}&short={}&name={}'.format(key, url.replace("%3A",":"), name)).json()['url']['shortLink']
    except Exception as e:
        print(str(e))
        r=url

    print(r)
    return r
