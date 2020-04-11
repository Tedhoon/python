def repeat(c, n):
    sketch = "+"+"---+"*n+"\n"+"|"+"   |"*n
    for i in range(0,c):
        print(sketch)
    print("+"+"---+"*n)


c = int(input())
n = int(input())

repeat(c, n)