def greet(name,prefix="你好"):
    return f"{prefix},{name}"

def total(*nums):
    print(f"收到的参数是:{nums}")
    return(sum(nums))

def show(**kw):
    print(f"收到的参数是:{kw}")
    for k,v in kw.items():
        print(f"{k}={v}")

print(greet('zxj'))
print(total(1,2,3))
d={'上海':222,'北京':111,'深圳':333}
show(**d)

