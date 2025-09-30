number_1 = int(input())
number_2 = int(input())

digits_3 = []

digits_3.append(0)
digits_3.append(0)
digits_3.append(0)

i = 2
while number_1 > 0:
	digit_1 = int(number_1 % 10)
	digits_3[i] += digit_1
	number_1 = int(number_1 / 10)
	i = i - 1

i = 2
while number_2 > 0:
	digit_2 = int(number_2 % 10)
	digits_3[i] = (digits_3[i] + digit_2) % 10
	number_2 = int(number_2 / 10)
	i = i - 1

flag = 0
for i in range(3):
	if (digits_3[i] == 0 and flag != 1):
		continue
	else:
		flag = 1
		print(digits_3[i], end="")