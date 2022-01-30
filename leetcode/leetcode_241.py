class Solution(object):
    def diffWaysToCompute(self, expression):
        if "*"  not in expression and "-" not in expression and "+" not in expression :
            return [expression]
        output = []
        for index, ex in enumerate(expression):
            if ex == '*' or ex == '-' or ex == "+":
                left = self.diffWaysToCompute(expression[:index])
                right = self.diffWaysToCompute(expression[index+1:])
                for l in left:
                    for r in right:
                        output.append(eval(str(l) + ex + str(r)))

        return output


# version2
import operator
class Solution:
    ops = {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
    }

    def diffWaysToCompute(self, expression: str) -> List[int]:
        check = False # if문 들어갔나 확인 용
        output = []
        for i,e in enumerate(expression):
            if e in self.ops:
                check = True
                a_list = self.diffWaysToCompute(expression[:i])
                b_list = self.diffWaysToCompute(expression[i+1:])
                for a in a_list:
                    for b in b_list:
                        output.append(self.ops[e](a,b))

        if not check:
            return [int(expression)]
        return output
