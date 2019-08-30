# codes = "1000011"
# previous_bit = ""
# answer = ""
# for bit in codes:
#     print("bit: ", bit)
#     print("previous_bit:", previous_bit)
#     print("answer:", answer)
#     print("---")
#     if bit != previous_bit:
#         if bit == "1":
#             answer += " 0 "
#         else:
#             answer += " 00 "
#     answer += "0"
#     previous_bit = bit
# print(answer[1:])
# print("0 0 00 0000 0 00")
# n = int(input())
# price = input()
# prices = price.split()
# maxloss = 0
# highprice = 0
# for i in prices:
#     if i > highprice:
#         highprice = i
#     if i - highprice < maxloss:
#         maxloss = i - highprice
#
# print(maxloss)

# prices = list(map(int, input().split()))
# print(prices)
import sys
import math

# msg = input()
# out=""
# bn=""
# b=""
#
# for c in msg:
#     bn += bin(ord(c))[2:].zfill(7) # bin 함수를 쓰면 처음에 0b가 있어서 슬라이스로 [2:]부터 출력
# print(bn)
# for c in bn:
#     if c == "1" != b:
#         out += " 0 "
#         b="1"
#     elif c == "0" != b:
#         out += " 00 "
#         b="0"
#     out += "0"
#
# print(out.strip())

import sys
import math


# width = int(input())  # the number of cells on the X axis
# height = int(input())  # the number of cells on the Y axis
# cells = [''] * height
# for y in range(height):
#     cells[y] = [''] * width
#     line = input()
#     print(line)
#     for x in range(width):
#         cells[y][x] = line[x]
# width = int(input())  # the number of cells on the X axis
# height = int(input())  # the number of cells on the Y axis
# lines = [input() for _ in range(height)]  # width characters, each either 0 or .
# print(lines)
# print(lines[0][0])
