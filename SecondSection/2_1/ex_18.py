purchase_count = int(input())
banknote = int(input())

digits = []

i = -1
while purchase_count > 0:
    digit = purchase_count % 10
    digits.append(digit)
    purchase_count = purchase_count // 10
    i += 1

result = 0
for item in digits[::-1]:
    result += item * 2 ** i
    i -= 1

print(banknote - result)