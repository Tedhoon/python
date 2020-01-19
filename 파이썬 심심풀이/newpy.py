arr = [1,1,3,3,0,1,1]

def solution(arr):
    
    solve = []
    flag = 1

    solve.append(arr[0])


    for i in range(1,len(arr)):
        if flag==1 and arr[i]!=arr[i-1]:
            solve.append(arr[i])
            flag=0

        if flag==0 and arr[i]!=arr[i-1]:
            flag =1
        
    return print(solve)

    # for i in range(len(arr)):

    #     if arr[i] not in solve:
    #         solve.append(arr[i])
        
    #     if arr[i+1]==arr[i]:
    #         pass

            
    #     if arr.count(i)==1:
    #         continue
    #     else :
    #         arr.remove(i)
    #     print(solve)

    

solution(arr)
    

    # 연속적인 것만 제거하는 거임!
