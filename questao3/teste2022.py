from skiplistlist import SkiplistList

l1 = SkiplistList()
l2 = SkiplistList()

for i in range(3):
    l1.add(i,i+1)

j=0
for i in range(3,6):
    l2.add(j,i+1)
    j+=1

print(f'Antes do metodo l1.absorb(l2) \n l1 = {l1}\n l2 = {l2}')

l1.absorb(l2)

print(f'Depois do metodo l1.absorb(l2) \n l1 = {l1}\n l2 = {l2}')


