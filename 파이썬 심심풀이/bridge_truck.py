sec = 0

current_weight = 0
current_truck = {
    current_truck_pk:end_time,

}

def cal_



def solution(bridge_length, weight, truck_weights):
   

    for pk, v in enumerate(truck_weights):
        if current_truck: # currnet_truck이 처음에는 length가 0이니까!
            current_weight = 0
            for truck_pk, end_time in current_truck.items():
                if end_time == sec: # 만약 시간이 끝난 애들이 있으면 dic에서 지워주고
                    del current_truck[truck_pk]
                else:
                    current_weight += truck_weights[truck_pk]
                
            if current_weight + v >= weight: # 만약 현재 버틸수 있는 다리무게보다 합친게 더 많으면!
                sec += 1
                # 다시 위 for문으로 돌아가야하는데 현재의 pk, v로 돌아가야함!


        

        sec += 1
        # 처음에 트럭이 지나가고
        currnet_truck[pk] = sec + bridge_length 
        # 현재 트럭의 pk: 끝나는 시간으로 딕셔너리에 저장

        if current_weight + v =< weight:
            current_weight += v



solution(2, 10, [7,4,5,6])