import requests
import bs4
from urllib import parse

INFO = {
    'id': 'USER_ID'
}

def get_html(url):
    """
    웹 사이트 주소를 입력 받아, html tag 를 읽어드려 반환한다.
    :param url: parsing target web url
    :return: html tag
    """
    response = requests.get(url)
    response.raise_for_status()

    return response.text

a = input()

c = 'https://opendict.korean.go.kr/search/searchResult?focus_name=query&query='
c = c + parse.quote(a) + '&dicType=1&wordMatch=Y&searchType=&currentPage=1&cateCode=&fieldCode=&spCode=&divSearch=search&infoType=confirm&rowsperPage=10&sort=W&side_data=0%7C104529'

html = get_html(c)
soup = bs4.BeautifulSoup(html, 'html.parser')

INFO_main = soup.select('div.search_result dd span')

for i in INFO_main:
    title = i.getText().strip()
    print("%s" %title)

