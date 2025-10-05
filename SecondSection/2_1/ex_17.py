purchase_count = int(input())
cost_in_binary = int(input())

digits = []

i = -1
while cost_in_binary > 0:
    digit = cost_in_binary % 10
    digits.append(digit)
    cost_in_binary = cost_in_binary // 10
    i += 1

result = 0
for item in digits[::-1]:
    result += item * 2 ** i
    i -= 1

print(purchase_count + result)