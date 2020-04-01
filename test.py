# def mark_bold(function):
#     def wrapper(string):
#         return '<b>' + function(string) + '</b>'
#     return wrapper

# def mark_italic(function):
#     def wrapper(string):
#         return '<i>' + function(string) + '</i>'
#     return wrapper


# @mark_bold
# def contents(string):
#     return string

# @mark_italic
# def contents2(string):
#     return string

# @mark_bold
# @mark_italic
# def contents3(string):
#     return string

# print (contents('안녕'))
# print (contents2('안녕'))
# print (contents3('안녕'))

#(4, 0,1,'2020-03-31 07:46:26.622585+00','2020-03-31 07:46:26.622585+00'),

mylist = [19,24,28,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112]
num = 0
# print(len(mylist))
for i in range(5,89):
    
    print(f"({num+5}, 0 , {mylist[num]}, '2020-03-31 07:46:26.622585+00','2020-03-31 07:46:26.622585+00'),")
    num+=1