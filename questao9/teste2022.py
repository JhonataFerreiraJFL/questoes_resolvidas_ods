from dllist import DLList

l1 = DLList()
l2 = DLList()

for i in range(6):
    l1.add(i,i+1)

l2.add(0,6)
l2.add(1,7)
l2.add(2,8)

print(f'Antes do metodo l1.mistura(l2) \nl1 era {l1} \nl2 era {l2}')

print(l1.mistura(l2))
