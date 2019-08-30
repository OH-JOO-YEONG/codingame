import sys
import math

# message = input()
#
# def to_binary(decimal):
#     binary = ""
#     while decimal > 0:
#         reminder = decimal % 2
#         binary += str(reminder)
#         decimal = decimal // 2
#     n = 7 - len(binary)
#     if n != 0:
#         for x in range(n):
#             binary += "0"
#     return binary[::-1]
#
# binary_string = ""
#
# for ch in message:
#     binary_string += to_binary(ord(ch))  # ord라는 문자를 아스키코드로 변환하는 ord함수가 있음

# codes = "1000011"
# previous_bit = ""
# count = 0
# answer = ""
# for bit in codes:
#     print("bit: ", bit)
#     print("previous_bit:", previous_bit)
#     print("count :", count)
#     print("---")
#     if bit != previous_bit and count > 0:
#         if previous_bit == "1":
#             answer += "0 "
#         else:
#             answer += "00 "
#         answer += "0" * count + " "
#         count = 0
#     count += 1
#     previous_bit = bit
#
# if previous_bit == "1":
#     answer += "0 "
# else:
#     answer += "00 "
# answer += "0" * count
# print(answer)

message = input()

def to_binary(decimal):
    binary = ""
    while decimal > 0:
        reminder = decimal % 2
        binary += str(reminder)
        decimal = decimal // 2
    n = 7 - len(binary)
    if n != 0:
        for x in range(n):
            binary += "0"
    return binary[::-1]

binary_string = ""

for ch in message:
    binary_string += to_binary(ord(ch))  # ord라는 문자를 아스키코드로 변환하는 ord함수가 있음

def chuck_norris_encoding(codes):
    previous_bit = ""
    answer = ""
    for bit in codes:
        if bit != previous_bit:
            if bit == "1":
                answer += " 0 "
            else:
                answer += " 00 "
        answer += "0"
        previous_bit = bit
    return answer[1:]
encode_message = chuck_norris_encoding(binary_string)

print(encode_message)


# msg = input()
# out=""
# bn=""
# b=""
#
# for c in msg:
#     bn += bin(ord(c))[2:].zfill(7) # bin 함수를 쓰면 처음에 0b가 있어서 슬라이스로 [2:]부터 출력
#
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


