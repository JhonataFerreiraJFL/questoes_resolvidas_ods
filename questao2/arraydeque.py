'''
An array-based list implementation with O(1+min{i,n-i}) amortized update time.

Stores the list in an array, a, so that the i'th list item is stored
at a[(j+i)%len(a)].

Uses a doubling strategy for resizing a when it becomes full or too empty.
'''
from utils import new_array
from base import BaseList

class ArrayDeque(BaseList):

    def __init__(self,x=0,iterable=[]):
        # o parametro opcional deve ser colocado (self,x,iterable=[])
        # deve-se colocar x = 0 para o python interpretar como opcional
        self._initialize(x)
        self.add_all(iterable)

    def _initialize(self,x):
        print(f'{x}')
        self.a = new_array(1)
        self.j = 0
        self.n = 0

    def get(self, i):
        if i < 0 or i >= self.n: raise IndexError()
        return self.a[(i+self.j)%len(self.a)]

    def set(self, i, x):
        if i < 0 or i >= self.n: raise IndexError()
        y = self.a[(i+self.j)%len(self.a)]
        self.a[(i+self.j)%len(self.a)] = x
        return y

    def add(self, i, x):
        if i < 0 or i > self.n: raise IndexError()
        if self.n == len(self.a): self._resize()
        """print('tamanho de self.a no começo')
        print(self.a)
        print('tamanho de self.n no começo')
        print(self.n)
        print('tamanho de self.j no começo')
        print(self.j)"""
        if i < self.n/2:
            self.j = (self.j-1) % len(self.a)
            for k in range(i):
                self.a[(self.j+k)%len(self.a)] = self.a[(self.j+k+1)%len(self.a)]
        else:
            for k in range(self.n, i, -1):
                self.a[(self.j+k)%len(self.a)] = self.a[(self.j+k-1)%len(self.a)]
        self.a[(self.j+i)%len(self.a)] = x
        self.n += 1
        """print('tamanho de self.a no final')
        print(self.a)
        print('tamanho de self.n no final')
        print(self.n)
        print('tamanho de j no final')
        print(self.j)"""

    def remove(self, i):
        if i < 0 or i >= self.n: raise IndexError()
        x = self.a[(self.j+i)%len(self.a)]
        """print('tamanho de self.a no começo')
        print(self.a)
        print('tamanho de self.n no começo')
        print(self.n)
        print('tamanho de self.j no começo')
        print(self.j)"""
        if i < self.n / 2:
            for k in range(i, 0, -1):
                self.a[(self.j+k)%len(self.a)] = self.a[(self.j+k-1)%len(self.a)]
            self.j = (self.j+1) % len(self.a)
        else:
            for k in range(i, self.n-1):
                self.a[(self.j+k)%len(self.a)] = self.a[(self.j+k+1)%len(self.a)]
        self.n -= 1
        """print('tamanho de self.a no final')
        print(self.a)
        print('tamanho de self.n no final')
        print(self.n)
        print('tamanho de j no final')
        print(self.j)"""
        if len(self.a) >= 3*self.n: self._resize()
        return x

    def _resize(self):
        b = new_array(max(1, 2*self.n))
        for k in range(self.n):
            b[k] = self.a[(self.j+k)%len(self.a)]
        self.a = b
        """print('tamanho de a depois do resize')
        print(self.a)"""
        self.j = 0
