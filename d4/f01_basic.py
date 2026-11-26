def is_even(n):
    if n%2==0:
        return True
    else:
        return False

def is_leap(y):
    if y%4==0 and y%100!=0:
        return True
    if y%400==0:
        return True
    return False

def is_prime(n):
    if n==1 or n==2 or n<=0: return False
    for i in range(2,n):
        if n%i==0: return False
    return True


print(is_even(14),is_leap(1900),is_prime(17))

