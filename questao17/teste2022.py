#from binaryheap import BinaryHeap
from binaryheap import BinaryHeap


vet = BinaryHeap()

vet.add(6)
vet.add(4)
vet.add(8)
vet.add(3)
vet.add(5)
vet.add(7)
vet.add(9)

print(vet)
print("\nObtain values")

vet.new_remove(3)

print(vet)
