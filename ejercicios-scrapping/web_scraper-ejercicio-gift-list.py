import requests
from bs4 import BeautifulSoup


def download_from_url(url, user_agent):
    print('Downloading:', url)
    user = {'User-Agent': user_agent}
    try:
        html = requests.get(url, headers=user)

    except ConnectionError as e:
        print('Download error:', e.reason)
        html = None
    return html

# Configuramos URL y `user-agent`
url = "http://pythonscraping.com/pages/page3.html"
agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'

# Obtenemos la página web y creamos objeto bs
webpage = download_from_url(url, agent)
bsObj = BeautifulSoup(webpage.text, 'html.parser')

# Obtenemos la tabla con el id que buscamos
gift_list = bsObj.find('table', {'id': 'giftList'})

for sibling in gift_list.tr.next_siblings:
    item = sibling.find('td')
    try:
        print(item.text)
    except AttributeError:
        continue

