# from operator import le


def mearge_sort(arr):
    
    if len(arr) == 1:
      return arr
    else:
        middle = len(arr) //2
        left = arr[:middle]
        right = arr[middle:]
        return mearge(mearge_sort(left),mearge_sort(right))

def mearge(left,right):
    combined = []
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            combined.append(left[l])
            print(left[l])
            l += 1
        else:
            combined.append(right[r])
            r += 1
    
    return combined + left[l:] + right[r:]

print(mearge_sort([5,7,2,8,9,1,10,21]))