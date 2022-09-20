# carrying the smallest num
def bubblesort(data):
    if len(data) == 0:
        return "It`s empty"
    if len(data) == 1:
        return data
    i = len(data)-2
    j = len(data)-1
    count = 0
    while True:
        print(data)
        if data[i] > data[j]:
            data[i], data[j] = data[j], data[i]
        if i == 0:
            i = len(data)-1
            j = len(data)
            count += 1
            if count == len(data)-1:
                return data
        i -= 1
        j -= 1


print(bubblesort([2,76,43,3,23,5,1]))
