import sys
print("请输入一个整数，判断奇偶数\n")
print("输入q进行退出")
while True:
	s=input()
	t=True
	if s=='q':
		break
	try:
		x=float(s)
		y=int(s)

		if not x==y:
			t=False
	except ValueError:
		t=False
	if t==False:
		print("请输入整数")
		continue
	if y<=0:
		y=-y
	if y%2==1 :
		print(f"{s}是一个奇数")
	else:
		print(f"{s}是一个偶数")
