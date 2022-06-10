from dllist import DLList

l1 = DLList()
for i in range(8):
    l1.add(i,i+1)
print('antes da metodo l1.impares()')
print(f'l1\n{l1}')
print(l1.impares())
