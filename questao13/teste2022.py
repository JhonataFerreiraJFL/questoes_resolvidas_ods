from arraydeque import ArrayDeque

l1 = ArrayDeque()

for i in range(12):
    l1.add(i,i)
print(l1)
inicio = 5
fim = 7
print(f'inicio {inicio}')
print(f'fim {fim}')
l1.remove_varios(inicio,fim)
print(l1)
