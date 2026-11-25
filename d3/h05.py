#交集（保序)
text1=input("输入第一组数组")
text2=input("输入第二组数组")

s1=text1.strip().replace(","," ").split()
s2=text2.strip().replace(","," ").split()

s=set(s1)&set(s2)
m=[]
for i in s1:
    if i in s and i not in m:
        m.append(i)
ms=map(int,m)
print(list(ms))
