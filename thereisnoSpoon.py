import sys
import math


def find_right_power_node(power_x, power_y, cells, width, height):
    for x in range(power_x + 1, width):
        if cells[power_y][x] == '0':
            return (x, power_y)
    return (-1, -1)

def find_lower_power_node(power_x, power_y, cells, width, height):
    for y in range(power_y + 1, height):
        if cells[y][power_x] == '0':
            return (power_x, y)
    return (-1, -1)

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
cells = [''] * height
for y in range(height):
    cells[y] = [''] * width
    line = input()
    for x in range(width):
        cells[y][x] = line[x]

for y in range(height):
    for x in range(width):
        if cells[y][x] == '0':
            right_x, right_y = find_right_power_node(x, y, cells, width, height)
            lower_x, lower_y = find_lower_power_node(x, y, cells, width, height)
            print("{0} {1} {2} {3} {4} {5}".format(x, y, right_x, right_y, lower_x, lower_y))




