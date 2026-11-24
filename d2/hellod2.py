a=[80,92,65]
print(a[0],a[-1],a[1:3],len(a))

a.append(100)
a.insert(1,70)
a.remove(65)
print(a[:])
print(sorted(a),sorted(a,reverse=True))
a.sort()
print(a[::-1],a[::2])
