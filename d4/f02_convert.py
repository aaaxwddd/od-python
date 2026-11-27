def c_to_f(c):
    return c*9/5+32

def f_to_c(f):
    return (f-32)*5/9

def seconds_to_hms(s):
    #return f"{s//3600:02d}:{s%3600//60:02d}:{s%60:02d}"
    h,rem=divmod(s,3600)
    m,sec=divomd(rem,60)
    return f"{h:02d}:{rem:02d}:{sec:02d}"
print(c_to_f(f_to_c(103)))
print(seconds_to_hms(3723))
