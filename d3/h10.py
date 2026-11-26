#最长连续序列
text=input("请输入你的数据")
nums=list(map(int,text.strip().replace(","," ").split()))

if not nums:
    print("0 ()")
else:
    s=set(nums)
    best_len=0
    best_start=0

    for x in s:
        if x-1 not in s:
            cur=x
            length=1
            while cur+1 in s:
                cur+=1
                length+=1
            if length>best_len:
                best_len=length
                best_start=x

    seq=list(range(best_start,best_start+best_len))
    print(f"{best_len}({','.join(map(str,seq))})")

