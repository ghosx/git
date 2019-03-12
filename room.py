import requests
import math
import time
import datetime

headers = {
    'Pragma': 'no-cache',
    'Origin': 'http://10.10.64.6:8080',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Cache-Control': 'no-cache',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'http://10.10.64.6:8080/Room',
    'DNT': '1',
}

today = time.strftime("%Y-%m-%d", time.localtime())
data = {
  'Date': today+'@'+today,
  'RoomBH': '0',
  'BuildBH': '0',
  'FloorNum': '0',
  'page': '1',
  'rows': '10'
}

while True:
    try:
        response = requests.post('http://10.10.64.6:8080/Room/GetUsingRoomList', headers=headers, data=data)
        if response.ok:
            total = response.json()['total']
            print(total)
            break
    except Exception as e:
        print(e)

pages = math.ceil(total / int(data['rows']))

while int(data['page'])<= pages:
    print(data['page'])
    try:
        response = requests.post('http://10.10.64.6:8080/Room/GetUsingRoomList', headers=headers, data=data)
        if response.ok:
            rows = response.json()['rows']
            for i in rows:
                print(i['B_Name']+'  '+i['RoomNum']+'  '+i['JT_NO'])
            data['page'] = str(int(data['page']) + 1)
            time.sleep(1)
    except Exception as e:
        print(e)



