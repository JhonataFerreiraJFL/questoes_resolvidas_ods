from arraydeque import ArrayDeque        
v = ArrayDeque()
for i in range(0,20):
    v.add(i,i+1)
print(v)
for i in range(0,10):
    v.remove(0)
print(v)


