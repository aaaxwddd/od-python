import sys
while True:
	text=input("请输入三个数,按q退出").strip()
	if text=='q':
		break
	strs=text.replace(","," ").split()
	
	if len(strs) !=3:
		print("请输入三个数")
		continue
	try:
		a=float(strs[0])
		b=float(strs[1])
		c=float(strs[2])
	except ValueError:
		print("输入的数据有误，请正确输入")
		continue
	if a>=b and a>=c:
		print("最大的数是：",a)
	elif a<=b and c<=b:
		print("最大的数是：",b)
	else:
		print("最大的数是：",c)
