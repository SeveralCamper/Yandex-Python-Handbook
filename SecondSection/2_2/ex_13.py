a = int(input())
b = int(input())
c = int(input())

digits_1 = []
digits_2 = []
digits_3 = []

while a > 0:
	digit = a % 10
	digits_1.append(digit)
	a = a // 10
	digit = b % 10
	digits_2.append(digit)
	b = b // 10
	digit = c % 10
	digits_3.append(digit)
	c = c // 10

if (digits_1[0] == digits_2[0] and digits_2[0] == digits_3[0]):
	print(digits_1[0])
else:
	print(digits_1[1])