# from random import randrange


# def claiming(number):
#     cashe = {}
#     cashe[1]=1
#     cashe[2]=2
#     for n in range(3,number+1):
#         cashe[n] = cashe[n-1] + cashe[n-2]
#     return cashe[n]

# print(claiming(4))

def best_stock(prices):
    buy = 0
    sell = 1
    max_profit = 0
    while sell <len(prices)-1:
        print(max_profit)
        if prices[buy] > prices[sell]:
            buy = sell
        else:
            profit= prices[sell]-prices[buy]
            max_profit = max(max_profit,profit)
        sell += 1
    return max_profit


print(best_stock([5,2,8,4,1]))
    