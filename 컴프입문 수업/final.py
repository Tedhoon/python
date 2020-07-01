# 그래도 시험이니까 한번은 쳐봐여지 ㅎ(모범생)

class Building(object):
    def __init__(self, floors):
        self._floors = [None]*floors
    def __setitem__(self, floor_number, data):
        print("__setitem__", floor_number)
        self._floors[floor_number] = data      
    def __getitem__(self, floor_number):
        print("__getitem__", floor_number)
        return self._floors[floor_number]
          

building1 = Building(4) # Construct a building with 4 floors
building1[0] = 'Reception'
building1[1] = 'ABC Corp'
building1[2] = 'DEF Inc'
print(building1[1])