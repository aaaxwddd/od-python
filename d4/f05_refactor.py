def max_next_max(nums):
    #最大和次大
    nums.sort()
    s1=[int(x) for x in nums]
    return (s1[-1],s1[-2])

def two_sum(nums,target):
    m={}
    for i,x in enumerate(nums):
        need=target-x
        if need in m:
            return([m[need],i])
        m[x]=i
    return []

print(max_next_max([1,3,5,7,9]))
print(max_next_max([2,4,6,8,10]))

print(two_sum([1,5,8,11,6],7))
print(two_sum([2,3,5,66,13],5))

