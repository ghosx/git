import os
import hashlib
import time
def main():
	start = time.time()
	file_del,file_num,md5_all,size_all = 0,0,[],[]
	path = input('path:')
	if os.path.isdir(path):
		for root,dirs,files in os.walk(path):
			for name in files:
				file = os.path.join(root,name)
				file_num += 1
				size = os.path.getsize(file)
				if size in size_all:
					with open(file,'rb') as f:
						md5 = hashlib.md5(f.read()).hexdigest()
						if md5 in md5_all:
							os.remove(file)
							file_del += 1
						else:
							md5_all.append(md5)
				else:
					size_all.append(size)
	else:
		print('路径错误!')
	end = time.time()
	print('共扫描'+str(file_num)+'个文件')
	print('共删除'+str(file_del)+'个文件')
	print('共耗时'+str(end-start)+'秒')
if __name__ == '__main__':
	main()
