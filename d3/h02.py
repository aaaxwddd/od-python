#第一次只出现一次的字符
text = input("请输入字符：")
s = text.strip().replace(",", " ").replace(""," ").split()
m={}
a=[]
for i in s:
    if i not in a:
        a.append(i)
    m[i]=m.get(i,0)+1
print(m)
for x in a:
    for k,v in m.items():
        if x==k and v==1:
            print(x)


