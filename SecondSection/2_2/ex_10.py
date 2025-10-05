number = int(input())

digits = []

while number > 0:
	digit = int(number % 10)
	digits.append(digit)
	number = number / 10

res_1 = digits[1] + digits[2]
res_2 = digits[0] + digits[1]

if (res_1 < res_2):
	print(f"{res_2}{res_1}")
else:
	print(f"{res_1}{res_2}")