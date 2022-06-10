from dllist import DLList

l1 = DLList()

for i in range(1000):
    l1.add(i,i+1)

print('antes')
print(l1)
print('depois')
l1.reverse()
