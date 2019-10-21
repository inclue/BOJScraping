#Get user's right problem count
#사용자별 맞은 갯수를 가져오는 크롤러

import requests
import re
from bs4 import BeautifulSoup

boj_id_list = ['your_boj_id']

for boj_id in boj_id_list:
    req = requests.get('https://www.acmicpc.net/user/%s'%boj_id)
    soup = BeautifulSoup(req.text, 'html.parser')
    right_problem = soup.find('a',{'href':'/status?user_id=%s&result_id=4'%boj_id})
    right_problem_count = re.sub('<[^>]*>','',str(right_problem))
    print(boj_id,right_problem_count)
