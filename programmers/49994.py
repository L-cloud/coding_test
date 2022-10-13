
def solution(dirs:str)->int:
    x,y = 5,5
    v = set()
    for c in dirs:
        if c == 'D':
            if x+1 < 11:
                if (x,y,x+1,y) not in v and (x+1,y,x,y) not in v:
                    v.add((x,y,x+1,y))
                x += 1
        elif c == 'L':
            if 0<= y -1:
                if (x,y,x,y-1) not in v and (x,y-1,x,y) not in v:
                    v.add((x,y,x,y-1))
                y -= 1

        elif c == 'R':
            if y+1 < 11:
                if (x,y,x,y+1) not in v and (x,y+1,x,y) not in v:
                    v.add((x,y,x,y+1))
                y+=1
        else:
            if 0<= x-1:
                if (x,y,x-1,y) not in v and (x-1,y,x,y) not in v:
                    v.add((x,y,x-1,y))
                x -= 1
    return len(v)
