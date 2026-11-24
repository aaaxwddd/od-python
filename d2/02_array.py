#及格率
text=input("请输入分数")
s=text.strip().replace(",","").split()
counts=0
try:
	for i in range(0,len(s)):
		if float(s[i])>100 or float(s[i])<0:
			print("请输入1~100的数")
			break
		if float(s[i])>=60:
			counts+=1
except ValueError:
	print("你的输入有误")

print(f"合格的人数为：{counts},合格率为{100*counts/len(s)}%")

