def main():
	"""
	a=(99,100)
	a[0]+=1
	print(a)
	"""
	#TypeError

	s=[('x',10),('y',20),('z',30)]
	print(s)
	s[1]=('y',25)
	print(s)

	o,value=s[0]
	return o,value

if __name__=="__main__":
	print(main())
