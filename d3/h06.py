#只出现一次的数
text=input("请输入你的数据")
s=text.strip().replace(","," ").split()
m={}
for i in s:
    if i not in m:
        m[i]=1
    else:
        m[i]+=1
print([item for item in m.items() if item[1]==1])
print([int(k) for k,v in m.items() if v==1])
