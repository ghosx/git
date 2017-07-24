import requests
from PIL import Image
from bs4 import BeautifulSoup
def get_code():
	code = requests.get('http://202.200.112.200/(ouxet5mlj13qdb55xl5kot45)/CheckCode.aspx').content
	with open('/home/he/1.gif','wb') as f:
		f.write(code)
def login(user,passwd,code):
	url = 'http://202.200.112.200/(ouxet5mlj13qdb55xl5kot45)/default2.aspx'
	r = requests.get(url).content
	soup = BeautifulSoup(r,'html.parser')
	__VIEWSTATE = soup.find('input',attrs={'name':'__VIEWSTATE'})['value']
	RadioButtonList1 = u"学生".encode('gb2312','replace')
	data = {
		'__VIEWSTATE':__VIEWSTATE,
		'txtUserName':user,
		'Textbox1':'',
		'TextBox2':passwd,
		'txtSecretCode':code,
		'RadioButtonList1':RadioButtonList1,
		'Button1':'',
		'lbLanguage':'',
		'hidPdrs':'',
		'hidsc':'',
		}
	headers = { 
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 
	'Accept-Language': 'zh-CN,zh;q=0.8', 
	'Connection': 'keep-alive', 
	'Content-Type': 'application/x-www-form-urlencoded', 
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36" 
	} 
	response = s.post('http://202.200.112.200/(ouxet5mlj13qdb55xl5kot45)/default2.aspx',data=data,headers=headers).content
	soup = BeautifulSoup(response,'html.parser')
	xm = soup.find('span',attrs={'id':'xhxm'}).string
	return xm.strip('同学')
def inf(xh,xm):
	headers = {
		'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Referer':'http://202.200.112.200/(ouxet5mlj13qdb55xl5kot45)/xs_main.aspx?xh='+str(xh),
		'Accept-Encoding':'gzip, deflate, sdch',
		'Accept-Language':'zh-CN,zh;q=0.8',
		}
	a = s.get('http://202.200.112.200/(ouxet5mlj13qdb55xl5kot45)/xsgrxx.aspx?xh='+str(xh)+'&xm='+str(xm)+'&gnmkdm=N121501',headers=headers).content
	soup = BeautifulSoup(a,'html.parser')
	xm = soup.find('span',attrs={'id':'xm'}).string
	xh = soup.find('span',attrs={'id':'xh'}).string
	xb = soup.find('span',attrs={'id':'lbl_xb'}).string
	rxrq = soup.find('span',attrs={'id':'lbl_rxrq'}).string
	csrq = soup.find('span',attrs={'id':'lbl_csrq'}).string
	byzx = soup.find('span',attrs={'id':'lbl_byzx'}).string
	mz = soup.find('span',attrs={'id':'lbl_mz'}).string
	zzmm = soup.find('span',attrs={'id':'lbl_zzmm'}).string
	lydq = soup.find('span',attrs={'id':'lbl_lydq'}).string
	yzbm = soup.find('span',attrs={'id':'lbl_yzbm'}).string
	zkzh = soup.find('span',attrs={'id':'lbl_zkzh'}).string
	sfzh = soup.find('span',attrs={'id':'lbl_sfzh'}).string
	cc = soup.find('span',attrs={'id':'lbl_CC'}).string
	xy = soup.find('span',attrs={'id':'lbl_xy'}).string
	xi = soup.find('span',attrs={'id':'lbl_xi'}).string
	zy = soup.find('span',attrs={'id':'lbl_zymc'}).string
	xzb = soup.find('span',attrs={'id':'lbl_xzb'}).string
	szj = soup.find('span',attrs={'id':'lbl_dqszj'}).string
	hsh = soup.find('span',attrs={'id':'lbl_ksh'}).string
	key = ['姓名','学号','性别','入学日期','出生日期','毕业中学','民族','政治面貌','来源地区',
	'邮政编码','准考证号','身份证号','学历层次','学院','系','专业','行政班','所在级','考生号']
	value = [xm,xh,xb,rxrq,csrq,byzx,mz,zzmm,lydq,yzbm,zkzh,sfzh,cc,xy,xi,zy,xzb,szj,hsh]
	information = dict(zip(key,value))
	return information
def grade(xh,xm):
	headers = {
		'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Referer':'http://202.200.112.200/(ouxet5mlj13qdb55xl5kot45)/xs_main.aspx?xh='+str(xh),
		'Accept-Encoding':'gzip, deflate, sdch',
		'Accept-Language':'zh-CN,zh;q=0.8',
	}

	url = 'http://202.200.112.200/(ouxet5mlj13qdb55xl5kot45)/xscj_gc.aspx?xh='+str(xh)+'&xm='+str(xm)+'&gnmkdm=N121605'
	r = requests.get(url,headers=headers).content
	soup = BeautifulSoup(r,'html.parser')
	__VIEWSTATE = soup.find('input',attrs={'name':'__VIEWSTATE'})['value']
	data = {
		'__VIEWSTATE':__VIEWSTATE,
		'ddlXN':'',
		'ddlXQ':'',
		'Button2':u"在校学习成绩查询".encode('gb2312','replace')
	}
	response = s.post(url,data=data,headers=headers).content
	soup = BeautifulSoup(response,'html.parser')
	xf = soup.find('span',attrs={'id':'xftj'}).b.string
	print(xf)
	tbody_2 = soup.find('table',attrs={'id':'TabTj'}).contents
	for child in tbody_2[7].children:
		print(child.string,end=' ')
	tbody_1 = soup.find('table',attrs={'class':'datelist'})
	for i in range(0,len(tbody_1.find_all('tr'))):
		for child in tbody_1.find_all('tr')[i].children:
			print(child.string,end='  ')
		print('\n')
def ke(xm,xh):
	headers = {
		'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Referer':'http://202.200.112.200/(ouxet5mlj13qdb55xl5kot45)/xs_main.aspx?xh='+str(xh),
		'Accept-Encoding':'gzip, deflate, sdch',
		'Accept-Language':'zh-CN,zh;q=0.8',
	}	
	url = 'http://202.200.112.200/(ouxet5mlj13qdb55xl5kot45)/xskbcx.aspx?xh='+str(xh)+'&xm='+str(xm)+'&gnmkdm=N121603'
	r = s.get(url,headers=headers).content
	soup = BeautifulSoup(r,'html.parser')
	bt = soup.find('table',attrs={'id':'Table1'})
	for i in range(0,len(bt.find_all('tr'))):
		for child in bt.find_all('tr')[i].children:
			print(child.string,end='   ')
		print('\n')
def xk(xh,xm):
	headers = {
		'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Referer':'http://202.200.112.200/(ouxet5mlj13qdb55xl5kot45)/xs_main.aspx?xh='+str(xh),
		'Accept-Encoding':'gzip, deflate, sdch',
		'Accept-Language':'zh-CN,zh;q=0.8',
	}		
	url = 'http://202.200.112.200/(3z23mo55ihq1kh45zimu1nq0)/xsxk.aspx?xh='+str(xh)+'&xm='+str(xm)+'&gnmkdm=N121101'
	r = s.get(url,headers=headers).content
	soup = BeautifulSoup(r,'html.parser')
	print(soup.prettify())
# 人生苦短，我用python

if __name__ == '__main__':
	print('''
		#########################################
		#\t欢迎使用西理工教务辅助软件\t#
		#\t  作者：heeeepin@gmail.com\t#
		#########################################
		''')
	s = requests.session()
	get_code()
	user = input('输入学号：')
	passwd = input('输入密码：')
	im = Image.open('/home/he/1.gif')
	im.show()
	code = input('输入验证码：')
	name = login(user,passwd,code)
	xm = name.encode('gb2312','replace')
	if name:
		while True:
			command = input('####################\n登陆成功！请选择：\n1.查询个人信息\n2.查询成绩\n3.测试\n###################\n')
			if command=='1':
				information = inf(user,xm)
				print(information)
				print('\n')
			elif command=='2':
				grade(user,xm)
			elif command=='3':
				xk(user,xm)
			else:
				print('命令错误啦~~~~(>_<)~~~~')
	else:
		print('登录失败╮(╯▽╰)╭')
