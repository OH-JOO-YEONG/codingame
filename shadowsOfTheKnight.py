# 이진탐색 문제
import sys
import math

w, h = [int(i) for i in input().split()]
n = int(input())
x, y = [int(i) for i in input().split()]

# 숫자맞추기 게임
# def binary_search(array, value):
#     low = 0
#     high = len(array) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#         if array[mid] > value:
#             high = mid - 1
#         elif array[mid] < value:
#             low = mid + 1
#         else:
#             return mid
#     return -1

low_y = 0
high_y = h - 1
left_x = 0
right_x = w - 1
while True:
    bomb_dir = input()
    if "U" in bomb_dir:
        high_y = y - 1
    elif "D" in bomb_dir:
        low_y = y + 1
    else:
        low_y = high_y = y

    if "R" in bomb_dir:
        left_x = x + 1
    elif "L" in bomb_dir:
        right_x = x - 1
    else:
        left_x = right_x = x

    x = (left_x + right_x) // 2
    y = (low_y + high_y) // 2

print("{} {}".format(x, y))

# cool algorithm
# w, h = [int(i) for i in input().split()]
# input()
# x0, y0 = [int(i) for i in input().split()]
#
# minX, minY, maxX, maxY = 0, 0, w, h
# while True:
#     bomb_dir = input()
#     for char in bomb_dir:
#         if char == "U":
#             maxY = y0
#         elif char == "D":
#             minY = y0
#         elif char == "R":
#             minX = x0
#         elif char == "L":
#             maxX = x0
#
#     x0 = (maxX + minX) >> 1
#     y0 = (maxY + minY) >> 1
#
#     print(x0, y0)
