total=0
sum1=0
sum2=0
sum3=0
for i in range(1,101):
	total+=i
	if i%2==0:
		sum1+=1
		sum2+=i
	else:
		sum3+=i

print(f"总和为{total}|偶数{sum1}个，偶数和{sum2}|奇数和{sum3}")

total=0
sum1=0
sum2=0
sum3=0
t=1
while t<=100:
	total+=t
	if t%2==0:
		sum1+=1
		sum2+=t
	else:
		sum3+=t
	t+=1
print(f"总和为{total}|偶数{sum1}个，偶数和{sum2}|奇数和{sum3}")
