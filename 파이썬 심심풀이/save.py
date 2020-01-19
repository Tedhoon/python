land = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
# land = [[1,5,3,5],[5,6,7,8],[4,3,2,1]]



# first_land = land[0]
# second_land = land[1]

# # 첫번째 max
# max(first_land) 

# # 두번째 max
# first_land.remove(max(first_land))
# print(first_land)


    

def solution(land):
    
    for num in range(1,len(land)):

        for i in range(0,4):
            
            if i != land[num-1].index(max(land[num-1])):
                land[num][i]+=max(land[num-1])

            # elif land[num-1].count(max(land[num-1]))!=1:
            #     land[num][i]+=max(land[num-1])
            else:
                continue
            if i==3:
                for k in range(0,4):
                    if k==land[num-1].index(max(land[num-1])):
                        land[num-1].remove(max(land[num-1]))
                        land[num][i] +=max(land[num-1])
                        
            
    return land


                

print(solution(land))

# def solution(land):
#     for num in range(1,len(land)):

#         for i,j in enumerate(land[num]):
             
#             if i != land[num-1].index(max(land[num-1])):
#                 j+=max(land[num-1])
#                 land[num][i] = j
#             else: 
#                 land[num-1].remove(max(land[num-1]))
#                 j+=max(land[num-1])
#                 land[num][i] = j
            
#     return print(land)

# solution(land)

# 이제 여기서 remove했을 때 그 전 리스트가 사라지지 않게 하면 됨.
