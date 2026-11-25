text1=input("请输入数据")
s1=text1.strip().replace(","," ").split()

text2=input("请输入数据")
s2=text2.strip().replace(","," ").split()

s=set(s1)-set(s2)
print(s)
m=[]

for i in s1:
    if i in s:
        if i not in m:
            m.append(int(i))
print(m)
