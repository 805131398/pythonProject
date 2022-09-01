import requests
import warnings
import time
import re


# 这个类用于获取深信服的数据
class Woc:

    def __init__(self):
        # 几个固定cookie变量
        self.vpn_list = None  # 用于解析html,table表格中的数据
        # 以下 cookie 请求相关数据
        self.DlanStatePageParam = "%26num2%3D50%26page%3D1"  # 请求数据
        self.selfcert_cookie = ""
        self.sinfor_session_id = ""
        self.anti_csrf = ""
        # 以上 cookie 请求相关数据
        # self.data 用于保存VPN连接名称和项目对应表中的数据,用于区分是专线还是5G
        self.data = {
            "fz_0001-fz0001": {
                "projectName": "石横265",  # 项目名称
                "ab_name": "sh265",
                "dedicatedIP": "112.53.83.168",  # 互联网专线ip
                "description": "石横265实时速率统计信息",
                "vpnConnName": "fz_0001-fz0001",  # VPN连接名称
                "isDedicatedIP": 0,
                "deviceType": "石横265VPN",
                'networkStatus': "断网",
                "retentionPolicyName": "...."
            },
            "fz_0002-fz_0002": {
                "projectName": "包钢500",  # 如上
                "ab_name": "bg500",
                "dedicatedIP": "39.154.128.90",
                "description": "包钢500实时速率统计信息",
                "vpnConnName": "fz_0002-fz_0002",
                "isDedicatedIP": 0,
                "deviceType": "包钢500VPN",
                'networkStatus': "断网",
                "retentionPolicyName": "...."
            }
        }

    def login(self):

        warnings.filterwarnings("ignore")

        url = "https://10.10.9.100/cgi-bin/login.cgi"

        payload = 'user=guoshun&password=%23********%23&read_and_agree=1&logintime=&program=3&ui=web&opr=in&in=&producttitle=WAN%20Accelerator&ZeroTouch=&pwd=GSxxh2022&authInfoCode=1&_csid=%3D%3D%3D%3D%3D%3D%3D1353760077*************1449311597----16764550---1374416101--&version=WANO9.5.8%3Cbr%3Ewano9.5.8.2108%20%20Build20191216%3Cbr%3Efwserver%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20M4.30_20091125%3Cbr%3Ecgi%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%204.30_20090227%3Cbr%3Ewebserver%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%204.1_20090227%3Cbr%3Elogs%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%204.1_20080301%3Cbr%3Edhcp5.0.75068%20Build20161029%3Cbr%3Ecluster%20%20%20%201.4_20101123%3Cbr%3ESNMPAGENT%201.0%20Build20110817%3Cbr%3Emdlan6.2.2.5809%20%20Build20191215%3Cbr%3EWOC9.5.8_J3x55hw_patch%20Build20200428%3Cbr%3EWOC9.X_HW_SP%20Build20200619%3Cbr%3ESP_WOC_JG01_901-958r1%20Build20210324%3Cbr%3ESP_WOC_JG_03_900-958r1%20Build20210324%3Cbr%3ESP_WOC_JG_04_500-958r1%20Build20210324%3Cbr%3ESP_WOC_JG_05_900-958r1%20Build20210324%3Cbr%3ESP_WOC_JG_06_900-958r1%20Build20210324%3Cbr%3EWOC9.5.8_woc_secure_check%20Build20200417%3Cbr%3EWOC9.5.8_WOC_gbdk_SP%20Build20200418%3Cbr%3EWOC9.5.8_woc_checkuplist%20Build20200421%3Cbr%3EWOC9.5.8_woc_newcheckuplist%20Build20200828%3Cbr%3ESP_WOC_woc_checkuplist%20Build20200928%3Cbr%3ESP_WOC_JG_0506_STAT%20Build20210609%3Cbr%3ESP_WOC_stat_01_700-958r1%20Build20210611%3Cbr%3ESP_WOC_HIDS_01_900-958r1%20Build20211013%3Cbr%3ESP_WOC_FORESEE_S801_800-959%20Build20220107%3Cbr%3ESP_WOC_FORESEE_S801_800-959_2%20Build20220222%3Cbr%3ESP_WOC_JG_08_900-959%20Build20220512%3Cbr%3ESP_WOC_JG_10_951-959%20Build20220810%3Cbr%3ESP_WOC_JG_11_900-959%20Build20220810%3Cbr%3Eupdate%20date%2022-08-13%3Cbr%3E&privateFlag=1'

        headers = {
            'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/104.0.5112.102Safari/537.36Edg/104.0.1293.63',
            'sec-ch-ua': '"Chromium";v="104","NotA;Brand";v="99","MicrosoftEdge";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", url, headers=headers, data=payload, verify=False)

        html_resource = response.content.decode('utf-8')

        result_csrf = re.finditer(r"\<input type\=\"hidden\" id\=\"result_csrf\" value\=\"(?P<result_csrf>.*?)\"\>",
                                  html_resource, re.S)

        for i in result_csrf:
            self.anti_csrf = i.group("result_csrf")

        for cookie in response.cookies:
            if cookie.name == 'sinfor_session_id':
                self.sinfor_session_id = cookie.value

        response.close()

        return self.sinfor_session_id

    def getVpn(self):

        # 忽略 ssl 警告信息
        warnings.filterwarnings("ignore")
        # 请求地址
        url = "https://10.10.9.100/cgi-bin/webui_vpn.cgi"

        headers = {
            "Cookie": f"language=zh_CN; select_tab=0; DlanStatePageParam={self.DlanStatePageParam};  sinfor_session_id={self.sinfor_session_id}; anti_csrf={self.anti_csrf}",
            'Referer': f'https://10.10.9.100/cgi-bin/wanacc_webui_sys.cgi?requestname=31&cmd=0&rand=444&woc_id={self.anti_csrf}',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63'
        }

        #  请求参数
        params = {
            "requestname": 16,
            "cmd": 0,
            "ver": "2108_chs",
            "anti_csrf": self.anti_csrf  # anti_csrf获取的是cookie中的参数
        }

        response = requests.request("GET", url, headers=headers, params=params, verify=False)
        content = response.content.decode('utf-8')

        # html 文本 解析, 获取tr中的内容
        result = re.finditer(
            r"\<tr onmouseover\=\'SelectRow\(this\)\' onkeydown\=\'SelectRow\(this\)\'\>(?P<tr>.*?)\<\/tr\>",
            content,
            re.S)

        tr_index = 0
        self.vpn_list = []
        for i in result:
            self.vpn_list.append({})
            td_result = re.finditer(r"td\>(?P<td>.*?)\<\/td\>", i.group("tr"), re.S)
            td_index = -1
            for td in td_result:
                td_index += 1
                if td_index == 1:
                    # 连接名称
                    self.vpn_list[tr_index]['conn_name'] = td.group("td")
                    # print("index-", td_index, "tr", tr_index, "-连接名称:", td.group("td"))
                elif td_index == 2:
                    # 用户名
                    self.vpn_list[tr_index]['username'] = td.group("td")
                    # print("index-", td_index, "-用户名:", td.group("td"))
                elif td_index == 4:
                    # 设备类型
                    self.vpn_list[tr_index]['d_type'] = td.group("td")
                    # print("index-", td_index, "-设备类型:", td.group("td"))
                elif td_index == 5:
                    # 实时流量
                    self.vpn_list[tr_index]['bytes_insight'] = td.group("td")
                    # print("index-", td_index, "-实时流量:", td.group("td"))
                    # 把实时流量分隔成上行瞬时流量和下行瞬时流量  单位使用Kbps
                    up_bytes_insight, down_bytes_insight = td.group("td").split('/', 1)
                    self.vpn_list[tr_index]['up_bytes_insight'] = self.getBps(up_bytes_insight)
                    self.vpn_list[tr_index]['down_bytes_insight'] = self.getBps(down_bytes_insight)
                elif td_index == 6:
                    # Internet IP
                    self.vpn_list[tr_index]['internet_ip'] = td.group("td")
                    # print("index-", td_index, "-internet_ip:", td.group("td"))
                elif td_index == 7:
                    # 内网 IP
                    self.vpn_list[tr_index]['network_ip'] = td.group("td")
                    # print("index-", td_index, "-内网 IP:", td.group("td"))
                elif td_index == 7:
                    # 接入时间
                    self.vpn_list[tr_index]['access_time'] = td.group("td")
                    # print("index-", td_index, "-接入时间:", td.group("td"))
                elif td_index == 8:
                    # 接入时间
                    self.vpn_list[tr_index]['access_time'] = td.group("td")
                    # print("index-", td_index, "-传输类型:", td.group("td"))
            tr_index = + 1
        response.close()
        return self.processing()

    def processing(self):
        for item in self.vpn_list:
            projectName = self.data[item['conn_name']]['projectName']  # 初始数据中保存的项目名称
            self.data[item['conn_name']]['up_bytes_insight'] = item['up_bytes_insight']
            self.data[item['conn_name']]['down_bytes_insight'] = item['down_bytes_insight']
            #  判断是不是专线 网络状态
            internet_ip = str(item['internet_ip']).replace('<br>', '')
            if str(self.data[item['conn_name']]['dedicatedIP']).__eq__(internet_ip):
                self.data[item['conn_name']]['isDedicatedIP'] = 1  # 是专线
                self.data[item['conn_name']]['networkStatus'] = "专线"  # 是专线
            else:
                self.data[item['conn_name']]['isDedicatedIP'] = 2  # 不是专线
                self.data[item['conn_name']]['networkStatus'] = "5G"  # 是专线
            # ip 保存，根据networkStatus | isDedicatedIP 判断ip是专线 ip 还是 5g IP
            self.data[item['conn_name']]['ip'] = internet_ip  # 不是专就是5G，保存起来
            # 输出一下看看当前状态
            # print(projectName, "当前瞬时上行流量是:", item['up_bytes_insight'], ",下行流量是:",
            #       item['down_bytes_insight'], "网络状态是:", self.data[item['conn_name']]['networkStatus'], ",IP:",
            #       self.data[item['conn_name']]['ip'])

        return self.data

    def getBps(self, bytes_insight):
        value = 0
        if "Gbps" in bytes_insight:
            #  * 1024 = Mbps * 1024 = Kbps
            value = float(re.search(r"(?P<value>\d.*?)Gbps", bytes_insight, re.S).group("value")) * 1024 * 1024
        elif "Mbps" in bytes_insight:
            # Mbps * 1024 = Kbps
            value = float(re.search(r"(?P<value>\d.*?)Mbps", bytes_insight, re.S).group("value")) * 1024
        elif "Kbps" in bytes_insight:
            # 不用转换了
            value = re.search(r"(?P<value>\d.*?)Kbps", bytes_insight, re.S).group("value")
        elif "bps" in bytes_insight:
            # bps / 1024 = Kbps
            value = float(re.search(r"(?P<value>\d.*?)bps", bytes_insight, re.S).group("value")) / 1024
        else:
            print("啥也没有")
        return value

    def saveHtml(self):
        print(self.vpn_list)
        # 将网页源代码,以html的形式保存到本地
        with open("vpn - " + time.time().__str__() + ".text", mode="w", encoding='utf-8') as f:
            f.write(self.vpn_list.__str__())  # 将源代码写入到文件
