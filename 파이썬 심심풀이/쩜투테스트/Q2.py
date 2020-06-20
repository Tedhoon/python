from Q1 import Calculator

class MaxLimitCalculator(Calculator):
    # 오버라이딩으로 해결
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100
    
cal = MaxLimitCalculator()

cal.add(50) # 50 더하기
cal.add(60) # 60 더하기
cal.add(10)

# cal
print(cal.value) # 100 출력