from dllist import DLList

l1 = DLList()

for i in range(21):
    l1.add(i,i+1)

print(f'l1 = {l1}')

print('feito split')

print(l1.split())
