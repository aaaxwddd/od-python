a=[3,5,8,2,6,7,1,4]

print(a)

print(sorted(a))
print(a)

print(a.sort())
print(a)

words=["app","apppuls","helloword","whereareyounow"]
print(words)
words.sort(key=len)
print(words)

students=[("张三",85),("李四",75),("王五",90)]
print(students.sort(key=lambda x:x[1]))
print(students)

