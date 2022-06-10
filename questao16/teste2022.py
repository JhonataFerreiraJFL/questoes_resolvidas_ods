from binarysearchtree import BinarySearchTree

l1 = BinarySearchTree()

l1.add(10)
l1.add(5)
l1.add(2)
l1.add(6)
l1.add(12)
l1.add(11)
l1.add(15)

print(l1)
print('pré ordem')
l1.pre_order()
print('pré in-ordem')
l1.in_order()
print('pós ordem')
l1.pos_order()

l1.descobrir_numero_pre()
l1.descobrir_numero_in()
l1.descobrir_numero_pos()
