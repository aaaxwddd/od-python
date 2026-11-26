def c_to_f(c):
    return c*9/5+32

def f_to_c(f):
    return (f-32)*5/9

def seconds_to_hms(s):
    a1=0
    b1=0
    c1=0
    a=s//3600
    b=(s%3600)//60
    c=s%60
    if a>=10:
        a1=a//10
        a=a%10
    if b>=10:
        b1=b//10
        b=b%10
    if c>=10:
        c1=c//10
        c=c%10
    return (f"{a1}{a}:{b1}{b}:{c1}{c}")

print(c_to_f(f_to_c(103)))
print(seconds_to_hms(3723))
