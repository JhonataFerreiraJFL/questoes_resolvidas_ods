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

    def impares(self):
        l2 = DLList()
        print(f'l2\n{l2}')
        w1 = l2.dummy
        wx = l2.dummy
        u1 = self.dummy.next
        u2 = u1.next
        u3 = u2.next
        while (u1.x != None) and (u2.x != None):
            u1.next = u3
            u3.prev = u1
            u2.prev = w1
            u2.next = wx
            w1.next = u2
            wx.prev = u2
            w1 = w1.next
            u1 = u3
            u2 = u3.next
            u3 = u2.next
            self.n -= 1
            l2.n +=1
        return f'Depois da metodo l1.impares() \nResultado de l1 foi {self} \nE o Resultado de l2 foi {l2}'
