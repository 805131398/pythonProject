import requests

import re

music163url = 'https://music.migu.cn/v3/music/top/jianjiao_newsong'
# headers 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47'
}

response = requests.get(url=music163url, headers=headers)
text = response.text
# print(response.text)
script = re.findall('"id":"(\d+)","name":"(.*?)"', response.text)
# [a-z]+ [0-9]+ [\u4e00-\u9fa5]
print(script)
