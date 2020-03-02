# https://qiita.com/gogotealove/items/11f9e83218926211083a
# 買い物パターンの全列挙
money = 300
items = (('orange', 100), ('apple', 200), ('grape', 300))
n = len(items)

for i in range(2 ** n):
    """こっからがポイント"""
    print("pattern: {}".format(i), end="")
    bag = []
    for j in range(n):
        if (i >> j & 1):
            bag.append(items[j][0])
    print(bag)
