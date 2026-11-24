text_1=input("请输入第一组数据")
text_2=input("请输入第二组数据")
s1=text_1.strip().replace(","," ").split()
s2=text_2.strip().replace(","," ").split()
print(sorted(s1+s2))
print(sorted(set(s1+s2)))


