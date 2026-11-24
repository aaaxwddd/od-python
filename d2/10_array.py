#移动零
text=input("请输入数据")
s=text.strip().replace(","," ").split()
s1=s
counts=0
countspuls=0
m=[]
n=[]
for i in range(0,len(s)):
	if s[i]=="0":
		counts+=1
		m.append(i)
for j in range(0,len(m)):
	s.pop(m[j])
	for k in range(0,len(m)):
		m[k]-=1
for y in range(1,counts+1):
	s.append("0")
print(s)
"""
遍历列表s，遇到零时进行计数counts+1,将当前下标位置记录到m中。
遍历列表m，将对应下标的s进行pop删除，然后将m中的下标位置进行减一操作
通过计数counts将0加到末尾
"""
for x in range(0,len(s1)):
	if not s1[x]=="0":
		n.append(s1[x])
		countspuls+=1
for z in range(0,len(s1)-countspuls):
	n.append("0")
print(n)
"""
直接记录非0数加入新数组
然后通过计数与列表长度的差值追加0到末尾
"""
