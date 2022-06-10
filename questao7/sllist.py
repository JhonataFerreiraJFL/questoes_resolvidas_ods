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
        if self.n == 0: return None
        x = self.head.x
        self.head = self.head.next
        self.n -= 1
        if self.n == 0:
            self.tail = None
        return x

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

    def troca(self,x,y):
        k1 = 0
        while k1 < 1:
            if x == y:
                return self
            if self.n == 0:
                return self
            k1 +=1
        u1 = self.head
        w1 = self.head
        p1 = 0
        p2 = 0
        while (u1.x is not x) and (p1 < self.n - 1):
            u1 = u1.next
            p1 +=1
        if u1.x == x:
            while (w1.x is not y) and (p2 < self.n - 1):
                w1 = w1.next
                p2 +=1
            if w1.x == y:
                #caso especial 1
                if p1 == 0 and p2 == 1:
                    u1.next = w1.next
                    w1.next = u1
                    self.head = w1
                    return self
                # caso especial 2
                if p2 == 0 and p1 == 1:
                    w1.next = u1.next
                    u1.next = w1
                    self.head = u1
                    return self
                i = p1
                if p1 == 0:
                    # troca x
                    if self.n == 0:
                        return None
                    u1.x = self.head.x
                    self.head = self.head.next
                    self.n -= 1
                    if self.n == 0:
                        self.tail = None
                    i = p2 -1
                    u = self.head
                    for _ in range(i-1):
                        u = u.next
                    w = u1
                    w.next = u.next
                    u.next = w
                    self.n += 1
                    # troca y
                    i = p2
                    u = self.head
                    for _ in range(i-1):
                        u = u.next
                    w1 = u.next
                    u.next = u.next.next
                    self.n -= 1
                    i = p1
                    u = w1
                    w1.next = self.head
                    self.head = w1
                    self.n += 1
                    return self
                #trocar y
                i = p2
                if p2 == 0:
                    # troca y
                    # remove y
                    if self.n == 0:
                        return None
                    w1.x = self.head.x
                    self.head = self.head.next
                    self.n -= 1
                    if self.n == 0:
                        self.tail = None
                    i = p1 -1
                    u = self.head
                    for _ in range(i-1):
                        u = u.next
                    w = w1
                    w.next = u.next
                    u.next = w
                    self.n += 1
                    # troca x
                    # adciona y
                    i = p1
                    u = self.head
                    for _ in range(i-1):
                        u = u.next
                    u1 = u.next
                    u.next = u.next.next
                    self.n -= 1
                    i = p2
                    u = u1
                    u1.next = self.head
                    self.head = u1
                    self.n += 1
                    return self
                # se x maior que Zero e y maior que zero
                else:
                    if p1 < p2:
                        i = p1
                        # troca x
                        # remove x
                        u = self.head
                        for _ in range(i-1):
                            u = u.next
                        w = u.next
                        u.next = u.next.next
                        self.n -= 1
                        # adciona x
                        i = p2 - 1
                        u = self.head
                        for _ in range(i-1):
                            u = u.next
                        w = u1
                        w.next = u.next
                        u.next = w
                        self.n += 1
                        # troca y
                        # remove y
                        i = p2
                        u = self.head
                        for _ in range(i-1):
                            u = u.next
                        w1 = u.next
                        u.next = u.next.next
                        self.n -= 1
                        # adciona y
                        i = p1
                        u = self.head
                        for _ in range(i-1):
                            u = u.next
                        w = w1
                        w.next = u.next
                        u.next = w
                        self.n += 1
                        return self
                    if p1>p2:
                        i = p1
                        # troca x
                        # remove x
                        u = self.head
                        for _ in range(i-1):
                            u = u.next
                        w = u.next
                        u.next = u.next.next
                        self.n -= 1
                        # adciona x
                        i = p2
                        u = self.head
                        for _ in range(i-1):
                            u = u.next
                        w = u1
                        w.next = u.next
                        u.next = w
                        self.n += 1
                        # troca y
                        # remove y
                        i = p2 + 1
                        u = self.head
                        for _ in range(i-1):
                            u = u.next
                        w1 = u.next
                        u.next = u.next.next
                        self.n -= 1
                        # adciona y
                        i = p1
                        u = self.head
                        for _ in range(i-1):
                            u = u.next
                        w = w1
                        w.next = u.next
                        u.next = w
                        self.n += 1

        return f'{self}'
