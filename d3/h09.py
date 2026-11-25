#找重复
text=input("请输入数据")
s=text.strip().replace(","," ").split()
m=set()
n=[]
for i in s:
    if i in m:
        n.append(i)
        continue
    m.add(i)
for i in set(n):
    print(i)
