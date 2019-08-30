'''
1. 최대 수익을 저장하는 변수를 만들고 0을 저장합니다.
2. 지금까지의 최저 주가를 저장하는 변수를 만들고 첫째 날의 주가를 기록합니다.
3. 둘째 날의 주가부터 마지막 날의 주가까지 반복합니다.
4. 반복하는 동안 그날의 주가에서 최저 주가를 뺀 값이 현재 최대 수익보다 크면 최대 수익 값을 그 값으로 고칩니다.
5. 그날의 주가가 최저 주가보다 낮으면 최저 주가 값을 그날의 주가로 고칩니다.
6. 처리할 날이 남았으면 4번 과정으로 돌아가 반복하고, 다 마쳤으면 최대 수익에 저장된 값을 결괏값으로 돌려주고 종료합니다.
'''

# n = int(input())
# prices = []
#
# for i in range(5):
#     price = int(input())
#     prices.append(price)
# print(prices)
# def stockloss(price):
#     n = len(price)
#     maxloss = 0
#     highprice = 0
#     for i in range(n):
#         if price[i] > highprice:
#             highprice = price[i]
#         if price[i] - highprice < maxloss:
#             maxloss = price[i] - highprice
#     return maxloss
# print(stockloss(prices))

n = int(input())
maxloss = 0
highprice = 0
for i in input().split():
    v = int(i)
    if v > highprice:
        highprice = v
    if v - highprice < maxloss:
        maxloss = v - highprice

print(maxloss)

# n = int(input())
# prices = list(map(int, input().split()))
#
# loss = 0
# high = prices[0]
#
# for p in prices:
#     high = max(high, p)
#     loss = min(loss, p - high)
#
# print(loss)

