nums = [-1,0,1,2,-1,-4,0,0,-5,-4]
class Solution:
    def threeSum(self, nums):
        res = set()
        p =[]
        n = []
        z =[]
        for num in nums:
            if num >0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)
        print(p)
        print(n)
        print(z)
        if 3 <= len(z):
            res.add((0,0,0))
        if 1 <= len(z):
            for p_num in p:
                if -(p_num) in n:
                    res.add((0,p_num,-(p_num)))
        positives = set(p)
        negatives = set(n)
        for i in range(len(negatives)):
            for j in range(i+1, len(positives)):
                n_sum = (n[i]+n[j])
                if -(n_sum) in positives:
                    res.add(tuple(sorted([n[i], n[j], -(n[i]+n[j])])))
        for i in range(len(positives)):
            for j in range(i+1, len(positives)):
                p_sum = (p[i]+p[j])
                if -(p_sum) in negatives:
                    res.add(tuple(sorted([p[i], p[j], -(p[i]+p[j])])))
        print(res)

s = Solution()
s.threeSum(nums)