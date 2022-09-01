# fanyi.baidu.com
import requests

url = 'https://fanyi.baidu.com/sug'
english_world = input("请输入你要搜索的英文单词 \n")
data = {
    "kw": english_world
}

# 携带参数发送请求
resp = requests.post(url, data)

print(resp)  # 响应的状态码
print(resp.json())  # 将服务器返回的内容直接处理成 json => dict
