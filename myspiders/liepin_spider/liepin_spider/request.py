from urllib import  request

base_url = 'https://www.liepin.com/zhaopin/?key=%E8%BF%90%E8%90%A5&init=1&d_sfrom=search_fp_bar'
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "www.liepin.com",
    "Referer": "https://c.liepin.com/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",

}
req = request.Request(base_url,headers=headers)
print(request.urlopen(req).read().decode('utf-8'))