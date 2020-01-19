participant= ["mislav", "stanko", "mislav", "ana"]
completion =["stanko", "ana", "mislav"]


# def solution(participant, completion):
#     participant.sort()
#     completion.sort()

#     for i in range(len(participant)-1):
#         print(i)


    

print(solution(participant,completion))

def solution(participant, completion):
    for i in completion:
        if i in participant:
            participant.remove(i)  
            print(participant) 
            
    return ''.join(participant)
            
solution(participant, completion)
    



    

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i,v in enumerate(participant):
        if i>len(participant):
            return participant[-1]
        if v==completion[i]:
            continue

        else:
            return v 

            
        
 
          
solution(participant, completion)
    
    

