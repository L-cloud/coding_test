def solution(myString:str)->str:
    return "".join([i if i >= 'l' else 'l' for i in myString])
