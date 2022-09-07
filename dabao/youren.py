import json
import math
import re
import time

import requests


def changeTime(allTime):
    day = 24 * 60 * 60
    hour = 60 * 60
    min = 60
    if allTime < 60:
        return "%d 秒" % math.ceil(allTime)
    elif allTime > day:
        days = divmod(allTime, day)
        return "%d 天, %s" % (int(days[0]), changeTime(days[1]))
    elif allTime > hour:
        hours = divmod(allTime, hour)
        return '%d 小时, %s' % (int(hours[0]), changeTime(hours[1]))
    else:
        mins = divmod(allTime, min)
        return "%d 分钟, %d 秒" % (int(mins[0]), math.ceil(mins[1]))


class YouRen:
    # 初始化登陆
    def __init__(self):
        self.html = ""
        url = "http://10.130.100.254/cgi-bin/luci"
        data = {
            "luci_username": "root",
            "luci_password": "root"
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70"
        }
        resp = requests.post(url=url, data=data, headers=headers, allow_redirects=False)
        self.cookie = resp.headers.get("Set-Cookie")
        self.location = resp.headers.get("Location")
        self.html = resp.content.decode("utf-8")
        resp.close()
        # self.iptables(cookie, location)

    # 状态总览,主机系统信息[运行时间,负载等],内存[可用数,空闲数,缓冲等],网络[在用的IPv4 WAN基本状态信息], DHCP分配信息
    def overview(self):
        getUrl = f"http://10.130.100.254/{self.location}/admin/status/overview"

        payload = {
            "status": 1,
        }

        sysauth = re.search(r"(?P<sysauth>.*?) path", self.cookie, re.S).group("sysauth")

        headers = {
            "Cookie": f"{sysauth} ckname=1-menu",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70"
        }

        resp = requests.get(getUrl, params=payload, headers=headers, allow_redirects=False)
        result = resp.json()
        # print(json.dumps(resp.json(), sort_keys=True, indent=4, separators=(',', ': ')))

        # print((result['memory']['free'] + result['memory']['buffered']) / 1024, "KB")
        # print(round(result['memory']['total'] / 1024, 0), "KB")

        # uptime = result['uptime']
        print(changeTime(275668))
        resp.close()

    # 网络接口 可以获取路由器LAN口以及WAN_5G和WAN_WIRED口的接收及发送的累计流量
    def network(self):
        url = f"http://10.130.100.254/{self.location}/admin/network/iface_status/lan,wan_5g,wan_wired"
        sysauth = re.search(r"(?P<sysauth>.*?) path", self.cookie, re.S).group("sysauth")
        headers = {
            "Cookie": f"{sysauth} ckname=1-menu",
            "Referer": f"http://10.130.100.254/cgi-bin/luci/{self.location}/admin/network/5g_config",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70"
        }
        resp = requests.get(url, params=None, headers=headers, allow_redirects=False)
        result = resp.json()

        # print(json.dumps(resp.json(), sort_keys=True, indent=4, separators=(',', ': ')))

    # 防火墙状态
    def iptables(self, cookie, location):
        getUrl = f"http://10.130.100.254/{self.location}/admin/status/iptables"
        payload = {}
        sysauth = re.search(r"(?P<sysauth>.*?) path", cookie, re.S).group("sysauth")
        headers = {
            "Cookie": f"{sysauth} ckname=1-menu",
            "Referer": f"http://10.130.100.254/cgi-bin/luci/{location}/admin/network/5g_config",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70"
        }

        resp = requests.get(getUrl, params=payload, headers=headers, allow_redirects=False)
        self.html = resp.content.decode("utf-8")
        self.saveHtml("iptables")
        resp.close()

    # 获取 5g_config 信息
    def fiveGenerationConfig(self):
        url = f"http://10.130.100.254/{self.location}/admin/network/5g_config"
        sysauth = re.search(r"(?P<sysauth>.*?) path", self.cookie, re.S).group("sysauth")
        headers = {
            "Cookie": f"{sysauth} ckname=1-menu",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70"
        }
        resp = requests.get(url, params=None, headers=headers, allow_redirects=False)
        html = resp.content.decode("utf-8")
        obj = re.compile(r"IMEI号:</td><td>(?P<IMEI>.*?)<tr>.*?SIM卡状态:</td><td>(?P<SIM_STATUS>.*?)</table>", re.S)
        IMEI = obj.search(html).group('IMEI')
        SIM_STATUS = obj.search(html).group('SIM_STATUS')
        print(IMEI, SIM_STATUS)
        # print(resp.content.decode("utf-8"))

    def saveHtml(self, name):
        # 将网页源代码,以html的形式保存到本地
        with open(f" {name} " + time.time().__str__() + ".html", mode="w", encoding='utf-8') as f:
            f.write(self.html.__str__())  # 将源代码写入到文件


if __name__ == '__main__':
    yr = YouRen()
    # yr.network()
    # yr.theOverview()
    yr.fiveGenerationConfig()
