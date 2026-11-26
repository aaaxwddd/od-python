def tokenize(text):
    words=text.strip().replace(","," ").replace("."," ").lower().split()
    return words
def count(words):
    #get版
    s1={}
    for word in words:
        s1[word]=s1.get(word,0)+1
    return s1

def top_k(d,k=5):
    return(sorted(d.items(),key=lambda x:x[1],reverse=True)[:5])

def main():
    for w,c in top_k(count(tokenize(input("请输入文本")))):
        print(w,c)

if __name__=="__main__":
    main()





"""
for word in words:
    if word in s:
        s[word]+=1
    else:
        s[word]=1
print(sorted(s.items(),key=lambda x:x[1],reverse=True)[:5])


"""
