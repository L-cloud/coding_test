# Defining main function
# def main(user_input : int) -> int:
#     n = 1
#     while 2**n < user_input:
#         n += 1
#     if 2**n == user_input:
#         return print(1)
#     return print(0)
#     # write your codes!
# if __name__ == "__main__":
#     user_input = int(input())
#     main(user_input)
#-------------------------------------
# Defining main function
# import collections
# from typing import List
#
# def main(user_input:List[int]) ->None:
#     num = [0 for _ in range(10)]
#     for i in range(user_input[0] + 1,user_input[1]):
#         count = collections.Counter(str(i))
#         for key, value in count.items():
#             while count[key] > 0:
#                 num[int(key)] += 1
#                 count[key] -= 1
#     print(' '.join(map(str, num)))
#     return
#     # write your codes!
#
# if __name__=="__main__":
#     user_input = list(map(int,input().split()))
#     main(user_input)

#----------------------------

# Defining main function
# import collections
# from typing import List
# def main(user_input : List[str]):
#     start,able_num,output = 1, int(user_input[1]),[0, 0]
#     q = collections.deque([])
#     for index, char in enumerate(user_input[2]):
#         if start > len(user_input[2]): # 금지된 문자가 계속 나와서 start 가 끝으로 갈 수 있으니
#             break
#         if char == user_input[0]:
#             q.append(index)
#             if len(q) > able_num:
#                 left_banned_char = q.popleft()
#                 while left_banned_char < len(user_input[2]) - 1 :
#                     if user_input[2][left_banned_char] != user_input[0]: #금지된 단어가 아님, left_banned_char 1부터 시작해서 인덱스 보다 큼
#                         break
#                     if q:
#                         if q[0]  <= left_banned_char : # C 2 CCAATATCAGTATA 같은 경우 c다음 또 c 로 가야함 금지된 단어가 아니더라도
#                             break
#                     left_banned_char += 1
#                 start = left_banned_char # new start point, 문제에서 인덱스 + 1로 되어있음
#         if index - start > output[1] - output[0]: #maximum_lengh
#             output = [start, index]
#     print([output[0]+1, output[1] - output[0] + 1])
#
# if __name__=="__main__":
#     user_input = list(input().split())
#     main(user_input)