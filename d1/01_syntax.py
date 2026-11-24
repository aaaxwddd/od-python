a=1
b=1.2
c='abc'
d=True
e=False
print(f"变量与类型:a={a},b={b},c={c},d={d},e={e}")
print(type(a),type(b),type(c),type(d),type(e))

f=int("3")+1
g=str(3)+"1"

print(f'f=int("3")+1,{f}')
print(f'g=str(3)+"1",{g}')
print(f==g)

text=input("请输入文本")
print("文本类型:",type(text))
h=1.23456789
print(f"h={h},保留两位小数：{h:.2f}")
print("for in range(1,6) \n range的三种写法:range(stop),range(start,stop),range(start,stop,step) 左闭右开，step为步长,i为变量名,for还可以用于遍历字符串、列表")
print("while 条件：\n   代码块\n 只要条件为True,就会一直执行；条件变为False时退出\n Python的循环可以带else，循环正常结束时（非break打断）执行，'break'：立即跳出整个循环，'continue'：跳过本次循环，进入下一次")
