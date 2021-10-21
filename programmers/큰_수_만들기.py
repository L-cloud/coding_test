def solution(number:str, k:int) -> str:
    number_list,current_index = [num for num in number],0
    while k > 0 :
        for i in range(current_index, len(number_list) - 1):
            if number_list[i] < number_list[i + 1]:
                if i > 1:
                    current_index = i - 1
                k -= 1
                number_list.remove(number_list[i]) # if value is duplicated remove funtion remvoe first value
                break
        else:
            break
    if len(number_list) > 0:
        return "".join(number_list[:len(number_list) - k])
    
    return ""
