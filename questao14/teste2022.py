from sllist import SLList

l1 = SLList()

l1.add(0,3)
l1.add(1,5)
l1.add(2,8)
l1.add(3,5)
l1.add(4,10)
l1.add(5,2)
l1.add(6,1)

"""
l1.add(0,10)
l1.add(1,9)
l1.add(2,8)
l1.add(3,7)
l1.add(4,6)
l1.add(5,5)
l1.add(6,4)
l1.add(7,3)
l1.add(8,2)
l1.add(9,1)
l1.add(10,0)
"""
print(l1)

l1.particiona(5)

print(l1)
