import requests,urllib,pymysql,time
class cet:
	"""
	CET4　CLASS
	python3 + requests,urllib,pymysql,time
	"""
	def __init__(self):
		super(cet, self).__init__()
	def findtype(self,num):
		'''这个方法是在官网js文件中找到的'''
		typelist = {"1":"英语四级","2": "英语六级","3": "日语四级","4": "日语六级","5": "德语四级","6": "德语六级","7": "俄语四级","8": "俄语六级","9": "法语四级"}
		return typelist[num[9:10]]
	def score(self,num,name):
		# time.sleep(2)　99宿舍特别容易boom!
		data="id=%s&name=%s"%(num,urllib.parse.quote(name.encode("gbk")))
		url="http://cet.99sushe.com/getscore"+num
		header={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
			"Host":"cet.99sushe.com",
			"Referer":"http://cet.99sushe.com/",
			"Cache-Control":"max-age=0",
			"Content-Length":"36",
			"Upgrade-Insecure-Requests":"1",
			"Origin":"http://cet.99sushe.com",
			"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			"Accept-Encoding":"gzip, deflate",
			"Content-Type":"application/x-www-form-urlencoded",
			"Accept-Language":"zh-CN,zh;q=0.8",
			"Connection":"keep-alive"}
		try:
			r=requests.post(url,headers=header,data=data,timeout=3).text.split(',')
			data = {'姓名':r[7],'准考证号':r[1],'总分':r[5],'听力':r[2],'阅读':r[3],'写作':r[4],'学校':r[6],'等级':findtype(num)}
			return data
		except:
			return False
	def update(self):
		try:
			conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1q23lyc45j',db='test',charset='utf8')
			cur = conn.cursor()
			cur.execute('SELECT * FROM cet')
			result = cur.fetchall()
			for r in result:
				inf = self.score(r[3][0:2],r[2])
				try:
					insert = "UPDATE `cet` SET total_score="+inf['总分']+",read_score="+inf['阅读']+",write_score="+inf['写作']+",listen_score="+inf['听力']+" WHERE zhunkaozhenghao="+inf['准考证号']
					cur.execute(insert)
					print(insert)
				except:
					print('fail')
		finally:
			conn.commit()
			cur.close()
			conn.close()
