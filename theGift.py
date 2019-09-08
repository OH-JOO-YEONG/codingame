# 탐욕알고리즘

# 연습문제
def moneyChangeCoins(money):
    coins = [500, 100, 50, 10]
    total_count = 0
    for coin in coins:
        if money >= coin:
            count = money // coin
            money -= coin * count
            total_count += count
    return  total_count

# 본 문제
n = int(input())
cost = int(input())
budgets = [int(input()) for i in range(n)]
budgets = sorted(budgets)
remaining = n
sum_budgets = 0

for i in range(n):
    sum_budgets += budgets[i]

if sum_budgets < cost:
    print("IMPOSSIBLE")

else:
    for i in range(n):
        avg = cost // remaining
        if budgets[i] < avg:
            cost -= budgets[i]
            print(budgets[i])
        else:
            cost -= avg
            print(avg)
        remaining -= 1

# smart algo
# N, price = map(int, (input(), input()))
# out = []
# budgets = sorted(int(input()) for i in range(N))
# for i in range(N, 0, -1):
#     share = min(price//i, budgets.pop(0))
#     price -= share
#     out += [share]
# print('IMPOSSIBLE' if price else '\n'.join(map(str, out)))
