from skiplistlist import SkiplistList

l1 = SkiplistList()

for i in range(20):
    l1.add(i,i+1)
indice = 10
print(f'Antes do metodo trucate \nl1 era{l1}')
print(f'Para i = {indice}')

print(l1.trucate(indice))
