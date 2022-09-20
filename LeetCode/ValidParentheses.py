m = "(("
t = "){"


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        starts = ["(","[","{"]
        ends = [")","]","}"]
        length = len(s)
        if length%2 != 0:
            return False
        for n in s:
            if n in starts:
                stack.append(n)
            else:
                if stack == []:
                    return False
                if starts[ends.index(n)] == stack.pop():
                    pass
                else:
                    return False
        if stack ==[]:
            return True
        else:
            return False


f = Solution()
print(f.isValid(t))