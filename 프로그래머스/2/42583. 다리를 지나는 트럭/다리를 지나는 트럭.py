def solution(bridge_length, weight, truck_weights):
    ans = 0
    bridge_queue = []
    bridge_weight = 0
    
    while truck_weights or bridge_queue:
        ans += 1
        
        if bridge_queue and bridge_queue[0][1] == ans: 
            bridge_weight -= bridge_queue[0][0]
            bridge_queue.pop(0)
        
        if truck_weights and bridge_weight + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            bridge_weight += truck
            bridge_queue.append((truck, bridge_length + ans))
        
    return ans
            
