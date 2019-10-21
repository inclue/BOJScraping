#Get users solved problem
#유저 ID를 가져와 해당 유저들이 푼 문제를 가져옴.

import requests
import re
import random
from bs4 import BeautifulSoup
from time import sleep

boj_id_list=[]
with open('boj_id.txt', 'r') as file_read:
    while True:
        line = file_read.readline().strip()
        if not line:
            break
        boj_id_list.append(line)
print("Number of BOJ User :", len(boj_id_list))

problem_set = set()
cnt=0
for boj_id in boj_id_list:
    cnt+=1
    print("ID :",boj_id,'(%d/%d)'%(cnt,len(boj_id_list)))
    sleep(random.random())
    req = requests.get('https://www.acmicpc.net/user/%s'%boj_id)
    soup = BeautifulSoup(req.text, 'html.parser')
    correct = list(map(lambda x:int(re.sub('<[^>]*>','',str(x))),
                soup.find('div',{'class':'panel-body'}).find_all('span',{'class':'problem_number'})))
    for p in correct:
        problem_set.add(p)

with open('boj_problem.txt', 'w') as file_write:
    problem_list = list(problem_set)
    problem_list.sort()
    print("Write problem list : %d problems solved"%len(problem_list))
    for problem in problem_list:
        file_write.write('%d\n'%problem)
