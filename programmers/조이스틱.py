def solution(name: str) -> int:
    if name == 'A' * len(name):
        return 0
    a,z, current_index,joy, left = ord('A'),ord('Z'), 0,0,False
    passed_num = 0
    while current_index < len(name) and not (left and name[current_index] == 'A'):
        if left:
            joy += min(abs(a - ord(name[current_index])), abs(z - ord(name[current_index])) + 1) + 1
            current_index -= 1
        else:  # go right
            if name[current_index] == 'A':
                a_num,inner_index = 1, current_index
                while inner_index < len(name) and name[inner_index] == 'A':
                    inner_index += 1
                    a_num += 1
                if passed_num < a_num:
                    left = True
                    joy += (passed_num - 1) # already cursor is moved to right so return to none a
                    current_index -= (passed_num + 1)
                else:
                    joy += 1
                    current_index += 1
                    passed_num += 1
            else:
                joy += min(abs(a - ord(name[current_index])), abs(z - ord(name[current_index])) + 1) + 1 # move right cursor
                current_index += 1
                passed_num += 1
    return joy - 1

a = solution() # input test case