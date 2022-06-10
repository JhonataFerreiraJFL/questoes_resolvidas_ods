from sllist import SLList

l1 = SLList()


l1.add(0,20)
l1.add(1,30)
l1.add(2,9)
l1.add(3,7)
l1.add(4,27)
l1.add(5,6)
l1.add(6,10)
print(l1)
x = 30
y = 20
print(f'troca x = {x} e y = {y}')
l1.troca(x,y)
print('resultado final')
print(l1)
# caso especial
#x = 1
#y = 2
