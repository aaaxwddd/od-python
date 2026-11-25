#两数之和
text=input("请输入数组")
s=text.strip().replace(","," ").split()
try:
    target=int(input("请输入目标"))
    nums=list(map(int,s))
except ValueError:
    print("输入错误")
m={} #建立target-x 的下标词典——差值：下标
ans=[] #用来存输出地址的
for i,x in enumerate(nums):
    if x in m:
        ans=[m[x],i]
        break
    m[target-x]=i
print(ans)
"""
#两数之和封装版
def two_sum(nums,target):
    m={}
    for i,x in enmumerate(nums):
        need=target-x
        if need in m:
            return([m[need],i])
        m[x]=i
    return []

print(two_sum(nums,target))


