from binarysearchtree import BinarySearchTree

l1 = BinarySearchTree()

l1.add(8)
l1.add(6)
l1.add(5)
l1.add(7)
l1.add(10)
l1.add(9)
l1.add(11)


print(l1)
x = 6
print(f'subarvore com raiz {x}')
l1.sub_binary_tree(x)
