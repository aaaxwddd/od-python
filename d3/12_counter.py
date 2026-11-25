from collections import Counter
text=input("请输入文本")
words=text.strip().replace(","," ").replace("."," ").lower().split()
counter=Counter(words)
print(counter)
print(counter.most_common(5))
