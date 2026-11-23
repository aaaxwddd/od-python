import sys
def convert(s):
	#把用户输入转成'原值=结果'字符串；非法输入返回None
	s=s.strip().replace(" ","")
	if len(s)<2:
		return None
	unit=s[-1].upper()
	if unit not in("C","F"):
		return None
	num_str=s[:-1]
	try:
		num=float(num_str)
	except ValueError:
		return None
	if unit=="C":
		result=num*9/5+32
		return (f"{num_str}{unit}={result:.1f}F")
	else:
		result=(num-32)*5/9
		return (f"{num_str}{unit}={result:.1f}C")


def main():
	print("温度转换（输入q退出）")
	while True:
		try:
			s=input("请输入温度")
		except EOFError:
			print()
			break
		if s.strip().lower()=="q":
			break
		out=convert(s)
		if out is None:
			print("格式错误,请输入类似100C、212F、37c的形式")
		else:
			print(out)

if __name__=="__main__":
	main()
