import requests
import bs4
from urllib import parse

def get_html(url):

    response = requests.get(url)
    response.raise_for_status()

    return response.text

while True: # 입력 대기
    a = input()
    if a == 'break': # 검색 종료 명령
        break
    c = 'https://opendict.korean.go.kr/search/searchResult?focus_name=query&query='
    c = c + parse.quote(a) + '&dicType=1&wordMatch=Y&searchType=&currentPage=1&cateCode=&fieldCode=&spCode=&divSearch=search&infoType=confirm&rowsperPage=10&sort=W&side_data=0%7C104529'

    html = get_html(c)
    soup = bs4.BeautifulSoup(html, 'html.parser')

    INFO_main = soup.select('div.search_result dd span')

    if not INFO_main: # 사전에 없는 단어를 검색한 경우 존재하지 않음을 사용자에게 출력
        print('없습니다.')

    else:
        for i in INFO_main:
            title = i.getText().strip()
            print("%s" %title)
