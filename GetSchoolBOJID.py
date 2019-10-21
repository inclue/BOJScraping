#Get School BOJ ID
#학교에 속한 모든 BOJ 회원 조회

import requests
import re
from bs4 import BeautifulSoup

#Get Page List
#학교 랭킹 페이지 링크 가져오기
req = requests.get('https://www.acmicpc.net/school/ranklist/368')
soup = BeautifulSoup(req.text, 'html.parser')
a_list = soup.find('ul',{'class':'pagination'}).find_all('a')
page_list = []
for a in a_list:
    page_list.append(a['href'])
#처음/마지막 링크 제거
del page_list[0]
del page_list[-1]

#BOJ ID 가져오기
write_file = open('boj_id.txt','w')
for page in page_list:
    req = requests.get('https://www.acmicpc.net%s'%page)
    soup = BeautifulSoup(req.text, 'html.parser')
    tr_list = soup.find('table',{'id':'ranklist'}).find('tbody').find_all('tr')
    for tr in tr_list:
        write_file.write(str(re.sub('<[^>]*>','',str(tr.find_all('td')[1]))) + '\n')
write_file.close()
