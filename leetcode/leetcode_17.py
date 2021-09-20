import itertools
class Solution(object):
    def letterCombinations(self, digits):
        if digits == "":
            return []
        phone = {2:["a","b","c"], 3: ["d","e","f"], 4:["g","h","i"], 5 :["j", "k", "l"], 6 : ["m", "n", "o"], \
                 7:["p","q","r","s"], 8: ["t", "u","v"], 9: ["w","x","y", "z"]}
        press_list =[]
        for digit in digits:
            press_list.append(phone[int(digit)])
        return list(map("".join,(itertools.product(*press_list))))