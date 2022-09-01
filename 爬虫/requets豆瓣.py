# movie.douban.com

import requests
import json

url = 'https://movie.douban.com/j/chart/top_list'

params = {
    "type": 24,
    "interval_id": "100:90",
    "action": '',
    "start": 0,
    "limit": 20
}
heads = {
    "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)"
                  "Chrome/104.0.5112.102Safari/537.36Edg/104.0.1293.63"
}
resp = requests.get(url=url, params=params, headers=heads)

y = json.dumps(resp.json(), sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False)
print(y)

# print(resp.json())
