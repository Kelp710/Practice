def mis_serch(nums):
    len_nums = len(nums)
    #find numbers not in the coutinue list
    for n in range(len_nums):
        if not 0 < nums[n] < len_nums:
            nums[n] = len_nums + 1
    # ensure the numbers that exsist by using index(if there is 1 index(1 -1) should be index(1-1)= negative)
    for n in range(len_nums):
        
        if 0< abs(nums[n]) < len_nums:
            nums[abs(nums[n])-1] *= -1
    # if there is positive number that index+1 shoul be the number we want
    for n in range(len_nums):
        if nums[n] > 0:
            return n + 1
    return len_nums + 1
    




print(mis_serch([3,2,5,-1,1]))