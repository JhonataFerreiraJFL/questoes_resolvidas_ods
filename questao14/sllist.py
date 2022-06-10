"""An implementation of a singly-linked list"""
from base import BaseList

class SLList(BaseList):

    class Node(object):
        def __init__(self, x):
            self.x = x
            self.next = None

    def __init__(self, iterable=[]):
        self._initialize()
        self.add_all(iterable)

    def _initialize(self):
        self.n = 0
        self.head = None
        self.tail = None

    def new_node(self, x):
        return SLList.Node(x)

    def _add(self,x):
        u = self.new_node(x)
        if self.n == 0:
            self.head = u
        else:
            self.tail.next = u
        self.tail = u
        self.n += 1
        return True

    def push(self,x):
        u = self.new_node(x)
        u.next = self.head
        self.head = u
        if self.n == 0:
            self.tail = u
        self.n += 1
        return x

    def append(self, x):
        u = self.new_node(x)
        if self.n == 0:
            self.head = u
        else:
            self.tail.next = u
        self.tail = u
        self.n += 1
        return True

    def get_node(self, i):
        u = self.head
        for _ in range(i):
            u = u.next
        return u

    def get(self, i):
        if i < 0 or i > self.n-1: raise IndexError()
        return self.get_node(i).x

    def set(self, i, x):
        if i < 0 or i > self.n-1: raise IndexError()
        u = self.get_node(i)
        y, u.x = u.x, x
        return y

    def add(self, i, x):
        if i < 0 or i > self.n: raise IndexError()
        if i == 0: self.push(x); return True
        u = self.head
        for _ in range(i-1):
            u = u.next
        w = self.new_node(x)
        w.next = u.next
        u.next = w
        self.n += 1
        return True

    def remove(self, i):
        if i < 0 or i > self.n-1: raise IndexError()
        if i == 0: return self.pop()
        u = self.head
        for _ in range(i-1):
            u = u.next
        w = u.next
        u.next = u.next.next
        self.n -= 1
        return w.x

    def pop(self):
        if self.n == 0: return None
        x = self.head.x
        self.head = self.head.next
        self.n -= 1
        if self.n == 0:
            self.tail = None
        return x

    def _remove(self):
        return self.pop()

    def __str__(self):
        s = "["
        u = self.head
        while u is not None:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __len__(self):
        return self.size()

    def particiona(self, t):
        ux = self.head
        while ux.next is not None:
            ux = ux.next
        self.tail = ux
        u0 = self.head
        u1 = u0.next
        u2 = u1.next
        while u1.x != ux.x:
            while u0.x >= t:
                u0.next = None
                self.tail.next = u0
                self.tail = u0
                self.head = u1
                u0 = u1
                u1 = u2
                u2 = u2.next
            if u1.x >= t:
                u0.next = None
                u1.next = None
                self.tail.next = u1
                self.tail = u1
                u0.next = u2
                u1 = u2
                u2 = u2.next
            else:
                u0 = u1
                u1 = u2
                u2 = u2.next
        return
