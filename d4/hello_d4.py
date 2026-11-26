def c_to_f(c):
    return c*9/s+32

def stats(nums):
    return min(nums),max(nums),sum(nums)/len(nums)

def greet(name,prefix="你好"):
    return f"{prefix},{name}}"

print(c_to_f(100),greet("小周",prefix="早上好"))
print(stats([80,92,65]))

