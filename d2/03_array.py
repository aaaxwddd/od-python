#最大和次大
text=input("请输入数据")
s=text.strip().replace(","," ").split()
s.sort()
print(s[-1])
print(s[-2])

s.sort(reverse=True)
print(s[0])
print(s[1])

