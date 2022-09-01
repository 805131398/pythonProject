# 安装requests
# pipinstallrequests
import requests

query = input("输入一个你喜欢的名称: \n")

url = f"https://www.sogou.com/web?query={query}"
# heads = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#     "Accept-Encoding": "gzip,deflate,br",
#     "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
#     "Cache-Control": "max-age=0",
#     "Connection": "keep-alive",
#     "Cookie": "IPLOC=CN3701;SUID=0242226F492CA20A000000006306DCE7;SUV=1661394152263160;browerV=3;osV=1;ABTEST=0|1661394153|v17;SNUID=3372135F3035D6374948654031EAA2BA;ld=wZllllllll20xH8rlllllpGpTn7lllllbhJjlkllll9lllllpylll5@@@@@@@@@@;sst0=405;LSTMV=1511%2C507;LCLKINT=9141",
#     "Host": "www.sogou.com",
#     "Referer": "https://www.sogou.com/",
#     "sec-ch-ua": "Chromium\";v=\"104\",\"NotA;Brand\";v=\"99\",\"MicrosoftEdge\";v=\"104",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "Windows",
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "same-origin",
#     "Sec-Fetch-User": "?1",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)"
#                   "Chrome/104.0.5112.102Safari/537.36Edg/104.0.1293.63"
# }
heads = {
    "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)"
                  "Chrome/104.0.5112.102Safari/537.36Edg/104.0.1293.63"
}
resp = requests.get(url, headers=heads)

print(resp)
print(resp.text)  # 获取响应内容,页面源代码
