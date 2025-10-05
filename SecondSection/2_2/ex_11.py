number = int(input())

digits = []

min = 10000
max = -1
mid = 0

while number > 0:
	digit = int(number % 10)
	digits.append(digit)
	number = number // 10

for digit in digits:
	if (digit > max):
		max = digit

	if (digit < min):
		min = digit

for digit in digits:
	if (max > digit > min):
		mid = digit

if (max + min == mid * 2):
	print("YES")
else:
	print("NO")