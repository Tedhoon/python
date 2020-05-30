class Car():
    def __init__(self):
        self.name="티코"
        self.len = "3m"
    def __str__(self):
        return self.name
    def openTop(self):
        return print(f{})

class MyCar(Car):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        myname = self.name
        mylen = self.len
        print(myname)
        print(mylen)

a = MyCar()

a