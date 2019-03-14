
class LinearMap(object):
    def __init__(self):
        self.items = []
    def add(self,k,v):
        self.items.append((k,v))
    def get(self,k):
        for key,val in self.items:
            if key == k:
                return val
        raise  KeyError

class BetterTable(object):

    def __init__(self,n=100):
        self.maps = []
        for i in range(n):
            self.maps.append(LinearMap())

    def linearmap(self):
        pass


if __name__ == '__main__':
    a = LinearMap()
    a.add("i",1)
    a.add("love",2)
    a.add("you",3)
    print(a.get("i"))
    print(a.get("love"))
    print(a.get("you"))
    print(2,3,3)
    print(0x233)