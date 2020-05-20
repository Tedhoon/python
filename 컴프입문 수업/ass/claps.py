import numpy

my_list=[]
def cal369(s):
    temp = str(s)
    for i in range(len(temp)):
        if int(temp[i]) in [3,6,9]:
            my_list.append('*')
    return cnt
    

if __name__ == "__main__":
    cnt = 0
    input_num = input()
    input_num_list= input_num.split()
    temp_list = list(range(int(input_num_list[0]), int(input_num_list[1])+1))
    result = [n for n in temp_list if cal369(n)]
    rs = len(my_list)
    print(rs)