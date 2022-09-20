

def filledOrders(order, k):
    sorted_orders = order.sort()
    k_stock = k
    count = 0
    for o in sorted_orders:
        if int o < k_sort:
            count += 1
            k_sort -= order
    return count

s =filledOrders([20,30], 30)
print(s)