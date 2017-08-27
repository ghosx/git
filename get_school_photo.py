import requests
import re

class photo(object):
	"""docstring for ClassName"""
	s = requests.session()
	def __init__(self, User,Passwd):
		super(photo, self).__init__()
		self.User = User
		self.Passwd =Passwd

	def login(self):
		url = 'http://ids.xaut.edu.cn/authserver/login?service=http://my.xaut.edu.cn/login.portal'
		html = s.get(url).text
		lt = re.search(r'name="lt" value="(\S+)"',html)[1]
		execution = re.search(r'name="execution" value="(\S+)"',html)[1]
		_eventId = re.search(r'name="_eventId" value="(\S+)"',html)[1]
		data = {'username':self.User,
				'password':self.Passwd,
				'lt':lt,
				'execution':execution,
				'_eventId':_eventId,}
		res = s.post('http://ids.xaut.edu.cn/authserver/login?service=http://my.xaut.edu.cn/login.portal',data=data,allow_redirects=False,headers=headers)
		ticket = res.headers['Location']
		s.get(s.get(ticket,allow_redirects=False).headers['Location'])
		headers['Host'] = 'my.xaut.edu.cn'
		headers['Referer'] = 'http://ids.xaut.edu.cn/authserver/login?service=http://my.xaut.edu.cn/index.portal'
		res = s.get(ticket.split()[0],allow_redirects=False,headers=headers)
		Location = res.headers['Location']
		s.get(Location.split()[0])
		return True  
	def id_list(self):
		with open('E:\students.txt','r') as f:
			for each_line in f:
				print(each_line)

a = photo('3161611083','077298')
a.id_list()