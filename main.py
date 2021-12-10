import flask
from ArangoDriver import ArangoDriver

class IterMixin(object):
    def __iter__(self):
        for attr, value in self.__dict__.iteritems():
            yield attr, value

for i in range(0,3):
    s = ArangoDriver.getInstance()
    print (s)

class Hamada():
    def __init__(self):
        self._from = ""
        self._to = ""
        self.ham = 10

#a = Hamada()

#print(type(vars(a)))

#for key, value in vars(a).items():
    #print(key, " -> ", value)