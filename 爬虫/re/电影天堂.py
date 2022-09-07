# 正则表达式
import io
import sys

import requests
import json
import re
import csv
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
domain = 'https://www.dytt8.net/html/gndy/index.html'

params = {

}
heads = {
    "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)"
                  "Chrome/104.0.5112.102Safari/537.36Edg/104.0.1293.63"
}
resp = requests.get(url=domain, params=params, headers=heads, verify=False)
html = resp.content.decode("gb2312")

obj = re.compile(
    '\[<a href="(?P<categoryUrl>.*?)">(?P<categoryName>.*?)</a>\]<a href=\'(?P<movieUrl>.*?)\'>(?P<movieName>.*?)</a><br/>',
    re.S)

result = obj.finditer(html)
f = open("dytt8.csv", mode="w", encoding='utf-8')
csvwriter = csv.writer(f)
csvwriter.writerow({"categoryUrl", "categoryName", "movieUrl", "movieName"})
for i in result:
    dict = i.groupdict()
    print(dict)
    csvwriter.writerow(dict.values())
f.close()
print("保存完成")
data = pd.read_csv("dytt8.csv")
res = data.dropna(how="all")
res.to_csv("dytt8.csv", index=False)