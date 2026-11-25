d={"apple":3,"banana":1}
d["apple"]+=1
d["cherry"]=d.get("cherry",0)+1
print(d,len(d),"apple" in d)
print(d.get("durian",0)

for k,v in d.items():
    print(k,v)

rank=sorted(d.items(),key=lamba kv: -kv[1])
print(rank)
s={1,2,2,3}
print(s,len(s),2 in s)

