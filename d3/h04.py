def group_anagrams(strs):
    m={}
    for i in strs:
        key="".join(sorted(i))
        if key not in  m:
            m[key]=[]
        m[key].append(i)
    return list(m.values())

text=input("请输入文本")
s=text.strip().replace(","," ").replace("."," ").lower().split()

print(group_anagrams(s))
