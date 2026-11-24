#去重保序
text=input("请输入数据")
s=text.strip().replace(","," ").split()
m=[]
for i in range(1,len(s)):
	if s[i-1] not in m:
		m.append(s[i-1])

n={x for x in s}
print(m)
print(set(s))
#print(list(dict.fromkey(n)))
print(s)
