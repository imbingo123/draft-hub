# Author: libin
# Date: 2021-07-20

class Solution:
    def isValid(self, s: str) -> bool:

        right_dict = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        # 空字符串的情况
        # if s == "":
        #     return True
        # 初始化一个栈, 并让第一个字符进栈
        stack = []

        for c in s:
            # 左括号，进栈
            if c in right_dict.values():
                stack.append(c)
            # 右括号，处理
            else:
                # 没有对应的右括号，返回 False
                length = len(stack)
                if length == 0:
                    return False
                # 有右括号，但不匹配，返回 False
                if stack[length - 1] != right_dict[c]:
                    return False
                # 有右括号，且匹配，去掉这个右括号
                if stack[length - 1] == right_dict[c]:
                    del stack[-1]
        
        # 栈空了，说明全部匹配了，返回 True; 否则说明有多余的左括号，返回 False
        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    s1 = "()[]{}"
    s2 = "()[]{}("
    s3 = "([{}])"
    s4 = ""
    s5 = "()"
    solution = Solution()
    res = solution.isValid(s5)
    print(res)



