from lib2to3.pytree import LeafPattern


di= "56"

class Solution:
    def letterCombinations(self, digits: str):
        ddict = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl',
                 '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        if len(digits) == 0:
            oldlist = []
        else:
            oldlist = ['']
            for d in digits:
                newlist = []
                for ss in ddict[d]:
                    for s in oldlist:
                        newlist.extend([s + ss])
                    # newlist.extend([s + ss for s in oldlist])
                print(oldlist)
                oldlist = newlist
                print(oldlist)
        return oldlist

s =Solution()
print(s.letterCombinations(di))