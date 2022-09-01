from urllib.request import urlopen

url = 'http://www.baidu.com/'
resp = urlopen(url)
# read = 网页的源代码
read = resp.read().decode("utf-8")
print(read)

with open("baidu.com.html", mode="w", encoding='utf-8') as f:
    f.write(read)  # 将源代码写入到文件

print("写入到 baidu.com.html 完成")
