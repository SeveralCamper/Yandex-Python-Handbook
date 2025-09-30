number = int(input())

digits = []

while number > 0:
	digit = int(number % 10)
	digits.append(digit)
	number = number / 10

print(f"{digits[2]}{digits[3]}{digits[0]}{digits[1]}")