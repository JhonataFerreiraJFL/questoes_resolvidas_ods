from dllist import DLList

l1 = DLList()

for i in range(5):
    l1.add(i,i+1)

print(l1)

l1.get(2)

print(l1)

l1.get(3)
print(l1)
