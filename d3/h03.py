from collections import Counter
text = input("请输入数组：")
s = text.strip().replace(",", " ").replace("."," ").lower().split()

counter=Counter(s)
print(counter)
print(counter.most_common(1))
