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