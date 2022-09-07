# 正则表达式
import io
import sys

import requests
import json
import re
import csv
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
url = 'https://movie.douban.com/top250'

params = {

}
heads = {
    "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)"
                  "Chrome/104.0.5112.102Safari/537.36Edg/104.0.1293.63"
}
resp = requests.get(url=url, params=params, headers=heads)
html = resp.text

print(html)

obj = re.compile(r'<span class="title">(?P<title>.*?)</span>.*?'
                 r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>', re.S)
result = obj.finditer(html)
f = open("data.csv", mode="w", encoding='utf-8')
csvwriter = csv.writer(f)
for it in result:
    dic = it.groupdict()
    csvwriter.writerow(dic.values())

f.close()
print("over")
data = pd.read_csv("data.csv")
res = data.dropna(how="all")
res.to_csv("data.csv", index=False)
