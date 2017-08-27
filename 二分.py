def f(x):
	'''
	帮一朋友写的二分法求根
	'''
	return 2*x**3-4*x**2+3*x-6
low = -10
high = 10
i = 1
while low < high:
	x = (low + high)/2
	print('第{}次二分'.format(i)+'x={}'.format(x))
	if f(x) == 0:
		print('\n方程的结果是X = ：',x)
		break
	elif f(x) < 0:
		low = x
	else
		high = x
	i += 1