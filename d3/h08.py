#是否能够重排成相同的词
#sorted(),将字母拆开重新排序，然后判断是否相等
from collections import Counter
text1=input("请输入第一个词")
s1=text1.strip().replace("."," ").replace(""," ").replace(","," ").split()

text2=input("请输入第二个词")
s2=text2.strip().replace("."," ").replace(""," ").replace(","," ").split()
m1="".join(sorted(s1))
m2="".join(sorted(s2))
print(m1==m2)
#其他方法
print(sorted(s1)==sorted(s2))


print(Counter(s1)==Counter(s2))
