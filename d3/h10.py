#最长连续序列

#验证错误，待修正
"""
text=input("请输入你的数据")
s=text.strip().replace(","," ").split()
m={}
s.sort()
n=set(s)
nums=[]
for i in s:
    if i not in nums:
        nums.append(i)

nums=sorted(set(nums))

a=[int(x) for x in nums]
count=0
for i in range(0,len(a)-1):
    if a[i]+1==a[i+1]:
        count+=1
    else:
        break
m[a[0]]=count


for i in range(1,len(a)):
    if a[i]-1!=a[i-1]:
        for j in range(i,len(a)-1):
            if a[j]+1==a[j+1]:
                m[a[i]]=m.get(a[i],0)+1
            else:
                break
    if a[i]-1==a[i-1]:
        m[a[i]]=m[a[i-1]]-1
(w,z)=max(m.items(),key=lambda x:x[1])
o=0
for i,x in enumerate(a):
    if x==w:
        o=i
t=[]
for i in range(0,z):
    t.append(a[o]+i)
print(f"{z} ({','.join(map(str,t))})")

"""
