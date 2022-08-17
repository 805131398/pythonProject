import requests
from bs4 import BeautifulSoup
import re
import time

myHeader = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
}
myCookies = {
    "Cookie": 'BIDUPSID=225F0FD0FC466B4E8B96232B603AD105; PSTM=1656302242; BAIDUID=225F0FD0FC466B4E6FDF9BF8767A711C:FG=1; BDUSS=m1mb2l6c05aNHpnYnl4Nzg5NEVhNGlTQldWTWoyVWdVcC1KSzZLUURhR3ZTeGxqRVFBQUFBJCQAAAAAAAAAAAEAAAD3F2yQwO7V8dPxyse49rGmsaYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK--8WKvvvFif; BDUSS_BFESS=m1mb2l6c05aNHpnYnl4Nzg5NEVhNGlTQldWTWoyVWdVcC1KSzZLUURhR3ZTeGxqRVFBQUFBJCQAAAAAAAAAAAEAAAD3F2yQwO7V8dPxyse49rGmsaYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK--8WKvvvFif; Hm_lvt_287705c8d9e2073d13275b18dbd746dc=1657594274,1658133429,1659171499,1660120117; STOKEN=77dff9a13123e2e524417b01d5560108500a43bfe7f7173fb541d826ada9a649; ZFY=YHglmRy3ZJp6QO8qzWHW9Lj1LidH:BO:ApboScjYv:A1eA:C; delPer=0; PSINO=1; BA_HECTOR=812080ah84052h8g0g0mi5kv1hflobv17; BAIDUID_BFESS=2CB99D30050927D83D0BEC11C91AFC93:FG=1; MCITY=-288%3A; BDRCVFR[NKud350Tv3c]=mk3SLVN4HKm; ZD_ENTRY=baidu; H_PS_PSSID=36547_36465_37115_36973_37140_36955_36949_36918_37003_36885_37135_26350_36862; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1658133429,1658969183,1660120117,1660616476; ab_sr=1.0.1_Mzk0NGNkYThiOGQyNmUxYTI5Nzg2NzU3MmI0NzRiMWQzODA3NzE3ODYxNmU5ODY0ZDdhZWZiYjBkYTVhNTkxMDA4ZGZlZmRiNjgzZmZmNjVhYzJkY2YxMDMzOTMyYmRkOTllZWNiMTE1NTNlMzBkZDA0N2RiMGZhNjk3N2FlYWJhZTYwZmI1NGJkMGZlODA2ZDZkMTRkZDczNmU0YmY0OQ==; st_data=79ee9d4e521bf7959c976d6cfbb576972b7fd5fb910948a748cd80003e9a4cd681c4c667bde20c3e621e8b07096fade218111cefcb4e25dd91057eda97e85c34e92979ee6f9b523799fb8437de194066f0475d5c89b814bcdedb5fc0d8d28ada; st_key_id=17; st_sign=26c426f3; BAIDU_WISE_UID=wapp_1660616476251_106; USER_JUMP=-1; RT="z=1&dm=baidu.com&si=t7mzd28k5za&ss=l6vk68bv&sl=2&tt=1n1&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=2cb&ul=1ecw&hd=1fah"; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1660616541'

}
url = "https://tieba.baidu.com/sign/add"


def getTblikes():
    i = 0
    url = "https://tieba.baidu.com/f/like/mylike"
    contain1 = BeautifulSoup(requests.get(url=url, cookies=myCookies, headers=myHeader).text, "html.parser")

    if contain1.find("div", attrs={"class": "pagination"}):
        pageNum = len(contain1.find("div", attrs={"class": "pagination"}).findAll("a"))
    else:
        pageNum = 2
    a = 1
    while a < pageNum:
        urlLike = f"https://tieba.baidu.com/f/like/mylike?&pn={a}"
        contain = BeautifulSoup(requests.get(url=urlLike, cookies=myCookies, headers=myHeader).text, "html.parser")
        first = contain.find_all("tr")
        for result in first[1:]:
            second = result.find_next("td")
            name = second.find_next("a")['title']
            singUp(name)
            time.sleep(5)
            i += 1
        a += 1
    print(f"签到完毕！总共签到完成{i}个贴吧")


def getTbs(name):
    urls = f"https://tieba.baidu.com/f?kw={name}"
    contain = BeautifulSoup(requests.get(urls, headers=myHeader, cookies=myCookies).text, "html.parser")
    first = contain.find_all("script")
    try:
        second = re.findall('\'tbs\': "(.*?)" ', str(first[1]))[0]
        return second
    finally:
        return re.findall('\'tbs\': "(.*?)" ', str(first[1]))


def singUp(tb):
    myDate = {
        "ie": "utf-8",
        "kw": tb,
        "tbs": getTbs(tb)
    }
    resp = requests.post(url, data=myDate, headers=myHeader, cookies=myCookies)
    result = re.findall('"error":"(.*?)"', str(resp.text))[0]
    if result.encode().decode("unicode_escape") == "":
        print(f"在{tb}签到成功了！！")
    else:
        print(f"在{tb}签到失败了，返回信息: " + result.encode().decode("unicode_escape"))


getTblikes()