# (Reverse Strings)
m = "aiueo"
print(m[::-1])

# it doesn`t work`
m = 3 >= s >= 8
# it works
m = 3<=s <= 8

ans = "seikai" if 6 == 2*3 else "machigai"

# Infinit num
num = float("inf")

# head of node will be 0, by return node.next it`ll be ok`
def node_pass():
    node = Node()
    return node.next
"When handling Nodes and Dummy Node Don`t forget to .next for each nodes "

# Chose not empty List, Node etc...
list1, list2 = [], [1,2,3]
temp = list1 or list2
print(temp)

# 3**3
log(9,3)==3

# Make hash map with amount of elements
s = "leetcode"
print(OrderedDict(Counter(s)).items())

# 右回転マトリックス
nums = [[1,2,3],[4,5,6],[7,8,9]]
right_rote = [list(n) for n in zip(*nums[::-1])]
print(right_rote)
# 左回転マトリックス
left_rote = [list(m) for m in zip(*nums)][::-1]
print(left_rote)

# True can be 1 False can be 0
n = 10
n += (not "asiu12".isalnum())
print(n)