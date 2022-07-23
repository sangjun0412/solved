import sys
input = sys.stdin.readline

raw = str(input().rstrip())


one_number = ""
raw_number = []

for i in raw:
    if i == '-' or i == '+':
        raw_number.append(one_number)
        raw_number.append(i)
        one_number = ""
    else:
        print(i)
        one_number += i
raw_number.append(one_number)


print(raw_number)

result = 0

change_number = []

for i in range(len(raw_number)):
    if i == '+':
        result += (int(raw_number[i-1]) + int(raw_number[i+1]))
    if i == '-':
        change_number.append(i)

print(change_number)
