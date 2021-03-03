from abc import ABC, abstractmethod

class Foo:
    def __getitem__(self, index):
        return self.get_iterator()
    def __len__(self):
        return self.__len__()
    def get_iterator(self):
        return iter(self)

class MyIterable(Foo):

    @abstractmethod
    def __iter__(self):

        while False:
            yield None

    def get_iterator(self):
        return self.__iter__()

    @classmethod
    def __subclasshook__(cls, C):
        if cls is MyIterable:
            if any("__iter__" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented

boy = MyIterable()
print(boy.__subclasshook__())

#print(man.__len__())

#print(boy.__getitem__())