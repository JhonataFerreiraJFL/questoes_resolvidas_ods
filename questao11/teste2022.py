from sllist import SLList

l1 = SLList()

for i in range(5):
    l1.add(i,i+1)
print(l1)
print(l1.reverse())
