def insertion_sort(data):
    if len(data) == 0:
        return "It`s empty"
    if len(data) == 1:
        return data
    max = 0
    search = 1
    while True:
        # Search is bigger than biggest number. serch shouldn`t move
        if data[max] <= data[search]:
            pass
        # Else compare it from the top
        elif data[search] < data[max]:
            for n in range(max+1):
                if data[search] < data[n]:
                    temp = data[search]
                    del data[search]
                    data.insert(n, temp)
        search += 1
        max += 1
        if max == len(data) -1:
            return data
    


print(insertion_sort([5,2,53,9,21,10,5]))

