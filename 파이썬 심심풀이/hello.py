land = [[1,2,3,5],[5,6,7,8]]
def solution(land):
    first_list = land[0]

    second_list = land[1]

    # for num in range(1, len(land)):
    #     # print(num)
        
        for i,j in enumerate(land[num]):
            
            # print(land[num-1])
            if i != land[num-1].index(max(land[num-1])):
                j+=max(land[num])
                land[num][i] = j
            else: 
                land[num-1].remove(max(land[num-1]))
                j+=max(land[num-1])
                land[num][i] = j
            

        
    return print(land)    

solution(land)

    # for i in land:
        
    #     print(i)
    #     max_index = i.index(max(i))
    #     # max_score = max(i.pop(idx))
        
        
    #     for idx,score in enumerate(i):
    #         return
            # print(idx,score)
# 전체 케이스를 떠올려봐
# 인덱스 처음에 1
            
    
    # print(land.split(','))
    # for i in range(len(land)):
        
        # print(land[i][1],land[i][2])



# -그전꺼랑 같은 인덱스 안됨
# -다 더함
# 다 비교 


