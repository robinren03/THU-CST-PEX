import requests
import time
import random
import sys
import os
from requests.exceptions import ConnectionError
def restart_program():
  python = sys.executable
  os.execl(python, python, * sys.argv)

cnt = 0
while(1):

  s = requests.Session()
  url = "http://166.111.214.78/Select_Select.php"
  payload = '/* lesson number */=/*lesson number*/&/* lesson number */=/*lesson number*/'
  headers = {
    'Host': '166.111.214.78',
    'Connection': 'keep-alive',
    'Content-Length': '9',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'http://166.111.214.78',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.63',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://166.111.214.78/Select_Select.php?weekselect=2',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cookie': 'PHPSESSID=/*Your cookie here */',
  }
  try:
    response = s.request("POST",url, headers=headers,data=payload,timeout=2)
  except ConnectionError:
    restart_program()
    break
  print("Success")
  time.sleep(0.1)
exit()

'''
编号对应表：
2 准稳态法测导热系数和比热
3 弹簧振子实验
5 透镜焦距的测定
6 三线摆和扭摆
9 示波器的原理和使用
10 阻尼振动与受迫振动
12 空气热容比的测量
13 弹性模量的测量、动力学法测杨氏模量
14 用传感器测空气相对压力系数
15 直流电桥测电阻
16 分光计的调节和色散曲线的测定
17 电学元件伏安特性的测量
18 液体粘度的测量
19 灵敏电流计
20 弦振动实验
'''