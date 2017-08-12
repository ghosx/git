import requests
import re
import urllib
def _type(num):
        return {"1":"英语四级","2": "英语六级","3": "日语四级","4": "日语六级","5": "德语四级","6": "德语六级","7": "俄语四级","8": "俄语六级","9": "法语四级"}[num[9:10]]
def score_xuexin(xm,zkzh):
    s = requests.session()
    s.get("http://www.chsi.com.cn/cet/")
    headers = {
        'Referer':'http://www.chsi.com.cn/cet/',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
    }
    url = 'http://www.chsi.com.cn/cet/query?zkzh={}&xm={}'.format(zkzh,urllib.parse.quote(xm))
    try:
        html = s.get(url,headers=headers).text
        html_table = re.findall(r"<table(.*?)</table", html,re.S)
        html_td = re.findall(r">(.*?)<", html_table[1],re.S)
        l = []
        for x in html_td:
            x = x.strip()
            x = x.rstrip('：')
            if x:
                l.append(x)
        return (l[3],l[7],l[9],l[12],l[16],l[20],l[24],l[26],l[29],l[33])           
    except:
        return False
def score_99sushe(name,num):
    data="id={}&name={}".format(num,urllib.parse.quote(name.encode("gbk")))
    url="http://cet.99sushe.com/getscore"+str(num)
    header={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Host":"cet.99sushe.com",
        "Referer":"http://cet.99sushe.com/",
        "Upgrade-Insecure-Requests":"1",
        "Origin":"http://cet.99sushe.com",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate",
        "Content-Type":"application/x-www-form-urlencoded",
        "Accept-Language":"zh-CN,zh;q=0.8",
        "Connection":"keep-alive"}
    try:
        r=requests.post(url,headers=header,data=data,timeout=3).text.split(',')
        return (r[7],r[6],_type(str(num)),r[1],r[5],r[2],r[3],r[4],r[9],r[10])
    except:
        return False
        
print(score_xuexin('张娜',610081162201503))
print(score_99sushe('张娜',610081162201503))
