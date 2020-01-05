#기본적으로 kwargs에 받아들이는 정보가 다담겨있다고 생각하면된다!
class Car():
    def __init__(self, **kwargs):
        self.name = "기본"
        self.wheels = 4
        self.windows = 4
        self.color = kwargs.get("color", "black")
        
    def __str__(self):
        return f"이 차는 {self.name}차 입니다!"


class Convertible(Car):
    def __init__(self , **kwargs):
        #기존의 __init__을 가져오고 싶으면 super로 부모를 호출 할 수 있음
        super().__init__(**kwargs)
        self.name = kwargs.get("name" , "외제차")
        self.openTop = kwargs.get("openTop" , "10s")

    #메서드 오버라이딩 가능(없으면 기존 것으로 나옴)
    def __str__(self):
        return f"이 차는 {self.color}색의 {self.name}차 입니다!"

    def openTopActivate(self):
        operation = "문이 열리는 중... 소요시간 : " + self.openTop
        return print(operation)

car = Car()
print(car)

porche = Convertible(name="포르쉐", color="red", openTop = '20s')
print(porche)

porche.openTopActivate()