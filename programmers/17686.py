from typing import List
def solution(files):
    # 영문 대소문자, 숫자, 공백, 마침표, - 으로만 이루어짐
    # HEAD, NUMBER, TAIL로 나뉘어짐
    head,number,tail = {},{},{}
    for file in files:
        make_h_n_t(file,head,number,tail)
    files.sort(key = lambda x:(str.upper(head[x]),int(number[x])))
    return files

def make_h_n_t(file:str,head:dict,number:dict,tail:dict) -> None:
    index = 0
    while not file[index].isnumeric():
        index += 1
    head[file] = file[:index]
    num = index
    while index < len(file) and  file[index].isnumeric():
        index += 1
    number[file] = file[num:index]
    tail[file] = file[index:]
    return
    
