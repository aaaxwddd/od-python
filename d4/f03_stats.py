def mean(nums):
    if nums==[]:return False
    return (sum(nums)/len(nums))

def max2(nums):
    if nums==[] :return False
    a=list(map(int,nums))
    return sorted(a,reverse=True)[1]

def count_above(nums,k):
    count=0
    m={}
    n=[]
    a=list(map(float,nums))
    for i in a:
        if i>k:
            m[i]=m.get(i,0)+1
            count+=1
            if i not in n:
                n.append(i)
    return count,n,m

print(f"{mean([1,2,3,4,3,2,1]):.2f}")
print(max2([1,3,5,7,9,11]))
count,n,m=count_above([1,2,3,4,5],3)
print(count,n,m)
