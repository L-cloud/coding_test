def solution(numbers, hand):
    matrix = {1:[1,1], 4:[2,1],7:[3,1],'*':[4,1],3:[1,3],6:[2,3],9:[3,3],'#':[4,3],2:[1,2],5:[2,2], 8:[3,2], 0 : [4,2]}
    L, R = [1,4,7],[3,6,9]
    l_hand, r_hand = "*", "#"
    answer = ''
    for number in numbers:
        if number in L:
            answer += 'L'
            l_hand = number
        elif number in R:
            answer += 'R'
            r_hand = number
        else:
            number_location = matrix[number]
            r = abs(number_location[0] - matrix[r_hand][0]) + abs(number_location[1] - matrix[r_hand][1])
            l = abs(number_location[0] - matrix[l_hand][0]) + abs(number_location[1] - matrix[l_hand][1])
            if r < l: # 오른손 더 가까움
                answer += 'R'
                r_hand = number
            elif l < r:
                answer += 'L'
                l_hand = number
            else:
                if hand == 'left':
                    answer += 'L'
                    l_hand = number
                else:
                    answer += 'R'
                    r_hand = number
            
    return answer
solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right')