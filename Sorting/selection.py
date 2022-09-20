def selection(data):
    if len(data) == 0:
        return "It`s empty"
    if len(data) == 1:
        return data
    min = 0
    forward = 1
    count = 0
    while True:
        print(min)

        print(f"f{forward}")
        if forward == len(data):
            return data
        if data[min] > data[forward]:
            min = forward
        if forward == len(data) -1:
            data[min],data[count] = data[count],data[min]
            count += 1
            min = count
            forward = count 
        forward += 1


print(selection([2,32,5,65,43,1,3,33,2,32,0,-1,234]))