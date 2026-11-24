#奇偶分离
text=input("请输入数据")
s=text.strip().replace(","," ").split()
s1=[]
s2=[]
try:
	for i in range(0,len(s)):
		if float(s[i])%2==0:
			s2.append(s[i])
		else:
			s1.append(s[i])
except ValueError:
	print("请正确输入数据")

print(f"奇数是{s1},偶数是{s2}")

