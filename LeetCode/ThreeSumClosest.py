nums = [98,70,-88,9]
target = -91
class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        diff =  float("inf")
        for i in range(len(nums)):
            start = 1+i
            end = len(nums) -1
            while start < end:
                sum = (nums[i]+nums[i+1]+nums[end])
                print(sum)
                if sum == target:
                    return target
                elif abs( target-sum )< diff:
                    diff = abs( target-sum )
                    answer = sum
                if sum > target:
                    end -= 1
                else:
                    start += 1
        return answer
                



s = Solution()
print(s.threeSumClosest(nums,target))

