import requests
import warnings

warnings.filterwarnings("ignore")

# url = 'https://10.10.9.100/cgi-bin/wanacc_webui_sys.cgi?requestname=31&cmd=0&rand=27&woc_id=94SI0pxpSa'
# url = 'https://10.10.9.100/cgi-bin/webui_vpn.cgi'
# url = 'https://10.10.9.100/cgi-bin/login.cgi?ui=web&opr=show&760'
# url = 'https://10.10.9.100/cgi-bin/login.cgis'

url = 'https://10.10.9.100/cgi-bin/cgi-bin/login.cgi?ui=web&opr=show&ver=2108_chs'
# url = 'https://10.10.9.100/cgi-bin/login.cgi?ui=web&opr=show&ver=2108_chs'

params = {
    "ui": "web",
    "opr": "show",
    "ver": "2108_chs"
}

headers = {

    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": """gzip, deflate, br""",
    "Accept-Language": """zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6""",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "language=zh_CN; sinfor_session_id=1661399782; anti_csrf=94SI0pxpSa; select_tab=0; DlanStatePageParam=%26num2%3D50%26page%3D1; cert_cookie=80709A79D6B16A3CADAE9B73252B23C7DF3F70C962CC64897E725C7B306C6012",
    "Host": "10.10.9.100",
    "sec-ch-ua": """Chromium;v=\"104\", \" Not A;Brand\";v=\"99\", \"Microsoft Edge\";v=\"104\"""",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63",
}

resp = requests.get(url=url, params=params, headers=headers, verify=False)

print(resp)

print(resp.content.decode('utf-8'))
#
with open("vpn.py.html", mode="w", encoding='utf-8') as f:
    f.write(resp.content.decode('utf-8'))  # 将源代码写入到文件
