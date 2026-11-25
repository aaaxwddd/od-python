#最大和次大
text=input("请输入数据")
s=text.strip().replace(","," ").split()
s.sort()
try:
    s1=[float(x) for x in s]
except ValueError:
    print("请正确输入")
print(s1[-1])
print(s1[-2])

s.sort(reverse=True)
print(s1[0])
print(s1[1])

