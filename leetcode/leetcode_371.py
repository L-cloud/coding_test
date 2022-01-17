class Solution:
    def getSum(self, a: int, b: int) -> int:
        a, b, carry = bin(a), bin(b), 0
        # 일단 부호 신경x
        a, b = a[2:], b[2:]
        i, j = len(a) - 1, len(b) - 1
        answer = ""
        while i > -1 and j > -1:
            tempt = int(a[i]) & int(b[j]) | carry
            num = int(a[i]) ^ int(b[j]) ^ carry
            answer = str(num) + answer
            carry = tempt
            i -= 1
            j -= 1
        while i > -1:
            if carry:
                tempt = carry & int(a[i])
                num = carry ^ int(a[i])
                carry = tempt
                answer = str(num) + answer
            else:
                answer = str(a[i]) + answer
            i -= 1
        while j > -1:
            if carry:
                tempt = carry & int(b[j])
                num = carry ^ int(b[j])
                carry = tempt
                answer = str(num) + answer
            else:
                answer = str(b[j]) + answer

            j -= 1

        answer = str(carry) + answer
        return int(answer, base=2)




