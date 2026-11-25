text=input("请输入文本")
words=text.strip().replace(","," ").replace("."," ").lower().split()
s={}
for word in words:
    if word in s:
        s[word]+=1
    else:
        s[word]=1
print(sorted(s.items(),key=lambda x:x[1],reverse=True)[:5])


#get版
s1={}
for word in words:
    s1[word]=s1.get(word,0)+1
print(sorted(s1.items(),key=lambda x:x[1],reverse=True)[:5])

