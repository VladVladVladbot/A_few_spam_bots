import requests
from bs4 import BeautifulSoup

URL = 'https://rule34.xxx/index.php?page=post&s=list&tags=all&pid='
kol = 1000  # Колличеаство фоток
id1 = 0
cars2 = []
con = 0
l1 = 0
o = 0
new_dict = {'https://wimg.rule34.xxx/thumbnails/5589/thumbnail_93979673a8447b8947700389d74771df7c0d1b6a.jpg?6362339'}

def get_html(url):
    r = requests.get(url)
    return r


def get_content(html):
    cars2 = []
    soup = BeautifulSoup(html, 'lxml')
    items = soup.findAll('span', class_='thumb')
    for item in items:
        cars2.append(item.find('img').get('src'))
    return cars2


def parse(con):
    html = get_html(URL + f'{con}')
    if html.status_code == 200:
        cars2 = get_content(html.text)
    else:
        print('Error')
    return cars2

while l1 < 50:
    l1 = l1 + 1
    for i in parse(con):
        new_dict.update({i})
        o = o+1
        print(o)
    con = con + 32
    print(new_dict)
print("Всё загружено")
new = iter(new_dict)