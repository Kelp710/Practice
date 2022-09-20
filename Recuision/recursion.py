def find_factor_by_recrusion(number):
    if number == 2:
        return 2
    return number * find_factor_by_recrusion(number-1)


def find_factor_by_iterative(number):
    answer = 1
    for n in range(1,number+1):
        answer *= n
    return answer

def fibonacci_recursion(n):
    if n < 2:
        return n
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

def fibonacci_iterative(n):
    array = [0,1]
    for num in range(2,n+1):
        array.append(array[num-1]+array[num-2])
    return array[n]


def reverse_iteration(data):
    reverse = []
    strip_data = data.strip()

    for n in range(len(strip_data)-1,-1,-1):
        reverse.append(strip_data[n])
    return "".join(reverse)

def reverse_recursion(data):
    if len(data) == 0:
        return data
    return reverse_recursion(data[1:]) + data[0]

print(reverse_recursion("koko 123456"))
print(sorted([1,6,4,54,3,21,2]))


