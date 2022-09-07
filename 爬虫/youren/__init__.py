import requests

if __name__ == '__main__':



    url = "http://10.130.100.254/cgi-bin/luci/;stok=43dd25764ba77f0b0235ce14d43160ab/admin/network/iface_status/lan,wan_5g"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70"
    }

    resp = requests.get(url, headers)

    print(resp.text)

