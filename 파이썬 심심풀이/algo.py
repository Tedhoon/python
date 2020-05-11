# 프로그래머스 모의고사

answers = [1,2,3,4,5]
as2 = [1,3,2,4,2]
def solution(answers):
    result_dic = {1:0,2:0,3:0} 
    man1 = [1,2,3,4,5]
    man2 = [2,1,2,3,2,4,2,5]
    man3 = [3,3,1,1,2,2,4,4,5,5]
    for i,v in enumerate(answers):
        if v == man1[i%5]:
            result_dic[1] += 1
        if v == man2[i%8]:
            result_dic[2] += 1
        if v == man3[i%10]:
            result_dic[3] += 1

    smarter = max(result_dic.values())
    result = []
    for k,v in result_dic.items():
        if v==smarter:
            result.append(k)

    return result

# 딕셔너리를 써보고 싶어서 일부러 적용해봄




# 밑에는 작년의 내가 풀었던 풀이 ㄷㄷ..



def solution(a):
    def function1(a):
        
        first=[]
        num=0
        while True:
            num+=1
            first.append(num)
            if num==5:
                num=0
                continue
            if len(a)==len(first):
                break
        return first

    def function2(a):
        
        second=[2]
        if len(a)==1:
            return second
        else:
            second.append(1)
            for i in range(len(a)-2):
                if second[i]==2:
                    second.append(2) 
                else: 
                    if second[i]==1:
                        second.append(3)
                    elif second[i]==3:
                        second.append(4)
                    elif second[i]==4:
                        second.append(5)
                    elif second[i]==5:
                        second.append(1)         
        return second


    def function3(a):
        
        third=[3]
        if len(a)==1:
            return print(third)
        else:
            third.append(3)
            for i in range(len(a)-2):
                if third[i]==third[i+1]:
                    if third[i]==3:
                        third.append(1)
                    elif third[i]==1:
                        third.append(2)

                    elif third[i]==2:
                        third.append(4)
                    elif third[i]==4:
                        third.append(3)
                else:
                    third.append(third[i+1])
        return third
    man1=function1(a)
    man2=function2(a)
    man3=function3(a)
    

    def score1(a):
        man1num=0
        for i in range(len(a)):    
            if man1[i]==a[i]:
                man1num+=1
        return man1num
            

    def score2(a):
        man2num=0
        for i in range(len(a)):    
            if man2[i]==a[i]:
                man2num+=1
        return man2num


    def score3(a):
        man3num=0
        for i in range(len(a)):    
            if man3[i]==a[i]:
                man3num+=1
        return man3num
    

    hello = [score1(a),score2(a),score3(a)]
    hi=[]

    
    for i in range(0,3):
        if hello[i]==max(hello):
            hi.append(i+1)
    return hi