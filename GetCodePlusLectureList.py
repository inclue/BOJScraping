# Get code.plus Lecture List
# cod.plus의 강의별 문제 목록을 크롤링

import requests
from bs4 import BeautifulSoup

url_list = ['LECTURE_URL']

for web_url in url_list:
    print('---------------') #Separator
    req = requests.get(web_url)
    soup = BeautifulSoup(req.text, 'html.parser')
    lecture_div = soup.find('div', {'class':'lecture-explain gist-preview markdown-table'})
    all_li = lecture_div.find_all('li')
    for li in all_li:
        #get problem number and problem name
        print(str(li).replace('<li><a href="https://www.acmicpc.net/problem/','').replace('</a></li>','').replace('">',' '))
