import sys

num = int(sys.stdin.readline())
power_of_num = 0
if num < 0:
    while (-2) ** power_of_num > num:
        power_of_num += 1

elif 0 < num:
    while (-2) ** power_of_num < num:
        power_of_num += 1
else:
    print(0)
    exit()

num_list = [0] * (power_of_num + 1)
