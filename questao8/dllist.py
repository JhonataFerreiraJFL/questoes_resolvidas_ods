"""A doubly-linked list implementation with O(1+min{i, n-i}) update time"""
from base import BaseList

class DLList(BaseList):

    class Node(object):
        def __init__(self, x):
            self.x = x
            self.next = None
            self.prev = None

    def __init__(self, iterable=[]):
        self._initialize()
        self.add_all(iterable)

    def _initialize(self):
        self.n = 0
        self.dummy = DLList.Node(None)
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy

    def get_node(self, i):
        if i < self.n/2:
            p = self.dummy.next
            for _ in range(i):
                p = p.next
        else:
            p = self.dummy
            for _ in range(self.n, i, -1):
                p = p.prev
        return p

    def get(self, i):
        if i < 0 or i >= self.n: raise IndexError()
        return self.get_node(i).x

    def set(self, i, x): #@ReservedAssignment
        if i < 0 or i >= self.n: raise IndexError()
        u = self.get_node(i)
        y = u.x
        u.x = x
        return y

    def _remove(self, w):
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1

    def remove(self, i):
        if i < 0 or i >= self.n: raise IndexError()
        self._remove(self.get_node(i))

    def add_before(self, w, x):
        u = DLList.Node(x)
        u.prev = w.prev
        u.next = w
        u.next.prev = u
        u.prev.next = u
        self.n += 1
        return u

    def add(self, i, x):
        if i < 0 or i > self.n:    raise IndexError()
        self.add_before(self.get_node(i), x)

    def __iter__(self):
        u = self.dummy.next
        while u != self.dummy:
            yield u.x
            u = u.next

    def split(self):
        if self.n == 0:
            return 'Não é posível usar o split'
        if self.n == 1:
            return 'Não é posível usar o split'
        l2 = DLList()
        w1 = self.dummy
        w2 = self.dummy.prev
        w2.next = None
        u1 = self.dummy.next
        if (self.n) % 2 == 1:
            p1 = 1
            while p1 <= (self.n + 1)/2:
                w1 = u1
                u1 = u1.next
                p1+=1
            w1.next = self.dummy
            self.dummy.prev = w1
            l2.dummy.next = u1
            u1.prev = l2.dummy
            p2 = 1
            while u1.next != None:
                u1 = u1.next
                p2 +=1
            u1.next = l2.dummy
            l2.dummy.prev = u1
            l2.n = p2
            self.n = p1 - 1
        else:
            p1 = 1
            while p1 <= (self.n/2):
                w1 = u1
                u1 = u1.next
                p1+=1
            w1.next = self.dummy
            self.dummy.prev = w1
            l2.dummy.next = u1
            u1.prev = l2.dummy
            p2 = 1
            while u1.next != None:
                u1 = u1.next
                p2 +=1
            u1.next = l2.dummy
            l2.dummy.prev = u1
            l2.n = p2
            self.n = p1 - 1
        print(f'l1 = {self} tamanho de l1 = {self.n}\nl2 = {l2} e o tamanho de l2 = {l2.n}')
        return 
