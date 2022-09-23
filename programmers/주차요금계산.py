from typing import List
def solution(fees:List[int], records:List[str]) -> List[int]:
    last_hour,answer = 23*60 + 59, []
    parking,p_k  = {},{} # p_k = 총 주차 시간
    for record in records:
        time,num,status = record.split()
        time = int(time.split(":")[0])*60 + int(time.split(":")[1])
        if status == 'IN':
            parking[num] = time
        else:
            time = time - parking[num]
            p_k[num] = p_k.get(num,0) + time 
            del parking[num]
    for num in parking:
        p_k[num] = p_k.get(num,0) + last_hour - parking[num]
    for key in sorted(p_k):
        print(key, p_k[key])
        if fees[0] < p_k[key]:
            fee = fees[1]
            p_k[key] -= fees[0]
            fee += ((p_k[key]) // fees[2]) * fees[3] if p_k[key] % fees[2] == 0  else ((p_k[key]) // fees[2]) * fees[3] + fees[3] 
            answer.append(fee)
        else:
            answer.append(fees[1])
    
    return answer
