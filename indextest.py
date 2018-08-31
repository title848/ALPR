a = [100,2,1,3,5,200,300,400,2,3,0,1,23,24,56,30,500,20,1000,3000]
#print(a.index(max(a)))
b = []
for i in range(0,9):
	b.append(a.index(max(a)))
	a[a.index(max(a))] = 0
	print(b)