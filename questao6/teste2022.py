from binarysearchtree import BinarySearchTree

l1 = BinarySearchTree()

for i in range(100, 0,-1):
    l1.add(i)
print(l1)
print(l1.leaf_son_left())
