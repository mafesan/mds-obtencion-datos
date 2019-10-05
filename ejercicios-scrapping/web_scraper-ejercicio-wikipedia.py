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
url = "https://es.wikipedia.org/wiki/Jose_Coronado"
agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'

# Obtenemos la página web y creamos objeto bs
webpage = download_from_url(url, agent)
bsObj = BeautifulSoup(webpage.text, 'html.parser')

# De todas las tablas, nos quedamos con la primera
# porque es la que contiene las películas
tables = bsObj.findAll('table', {'class': 'wikitable'})
movies = tables[0]

# Imprimimos la URL de las películas que tienen artículo
for item in movies.tr.next_siblings:
    a_element = item.find('a')
    try:
        if 'title' in a_element.attrs:
            extracted_url = a_element.attrs['href']
            if '/wiki/' in extracted_url:
                print(extracted_url)
    except Exception:
        continue
