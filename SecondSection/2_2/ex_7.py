number = int(input())

digits = []

while number > 0:
	digit = number % 10
	digits.append(digit)
	number = number // 10

if (digits[0] == digits[3] and digits[1] == digits[2]):
	print('YES')
else:
	print("NO")