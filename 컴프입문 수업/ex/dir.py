a=1

print(dir())
#['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a']
print(id(a))
#1347740432(메모리 주소)
print(__name__)
#__main__

# 활용
def main():
    activate()

if __name__ == "__main__":
    main()

#사실 1커밋을 하기 위해서 썻다능