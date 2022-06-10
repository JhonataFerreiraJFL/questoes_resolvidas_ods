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
        # modificacao para returnar o self vazio
        if u is None:
            return self
        while u != self.dummy:
            yield u.x
            u = u.next

    def mistura(self, l2):
        u0 = self.dummy
        u1 = u0.next
        u2 = u1.next
        u3 = u2.next
        uy = self.dummy
        w0 = l2.dummy
        w1 = w0.next
        w2 = w1.next
        wy = w0.prev
        w0.next = None
        w0.prev = None
        tot =  l2.n - self.n
        if self.n > 0:
            while w1.x is not None and u1.x is not None:
                u1.next = w1
                w1.prev = u1
                w1.next = u2
                u2.prev = w1
                u1 = u2
                u2 = u3
                u3 = u3.next
                w1 = w2
                w2 = w2.next
                uy = self.dummy.prev
                self.n+=1
                l2.n -=1
            if tot>=1:
                uy.next = w1
                w1.prev = uy
                wy.next = u0
                self.n += tot
                l2.n -= tot
        else:
            w1.prev = uy
            uy.prev = wy
            uy.next = w1
            wy.next = uy
            self.n = l2.n
            l2.n = 0
        print(f'Depois do metodo l1.mistura(l2) \nl1 = {self} \nl2 = {l2}')
        return 
