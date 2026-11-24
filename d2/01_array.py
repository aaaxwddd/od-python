#平均分
while True:
	print("平均数，输入q退出")
	text=input("请输入分数")
	m=text.lower()
	if m == 'q':
		break

	s=text.strip().replace(","," ").split()
	x=0
	try:
		for i in range(0,len(s)):
			x+=float(s[i])
	except ValueError:
		print("请输入数字")
	result=x/len(s)
	print(f"{result:.1f}")
