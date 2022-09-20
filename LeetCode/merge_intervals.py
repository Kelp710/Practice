class Solution:
    def merge(self, intervals):
        # Sort the list by list[i][0]
        sorted_list = sorted(intervals, key=lambda number: number[0])
        i = 0
        # Compare List of index i and i+1
        while True:
            print(sorted_list)
            if i >= len(sorted_list)-1:
                    return sorted_list
            if sorted_list[i][0] == sorted_list[i+1][0] and sorted_list[i][1] > sorted_list[i+1][1]:
                sorted_list[i], sorted_list[i+1] = sorted_list[i+1], sorted_list[i]

            if sorted_list[i+1][0] <= sorted_list[i][1] <= sorted_list[i+1][1]:
                sorted_list[i+1] = [sorted_list[i][0],sorted_list[i+1][1]]
                del sorted_list[i] 
            elif sorted_list[i][1] > sorted_list[i+1][1]:
                sorted_list[i+1] = [sorted_list[i][0],sorted_list[i][1]]
                del sorted_list[i] 
            else:
                i += 1
        

                


        
