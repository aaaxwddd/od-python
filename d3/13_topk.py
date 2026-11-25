text=input("请输入数组")
s=text.strip().replace(","," ").split()
n={}
try:
    for i in s:
        if i not in n:
            n[i]=1
        else:
            n[i]+=1
    print(sorted(n.items(),key=lambda x:(-x[1],float(x[0])))[:3])
except:
    print("请正确输入")

