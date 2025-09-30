mass_1 = []
mass_2 = []
mass_3 = []

number_1= int(input())
number_2 = int(input())
result = 0

flag = 0
while number_1 > 0 or number_2 > 0:
	mass_1.append(number_1 % 10)
	mass_2.append(number_2 % 10)

	res = ((number_1 % 10) + (number_2 % 10)) % 10
	if (res == 0 and flag != 1):
		flag = 1
	else:
		mass_3.append(res)

	number_1 = number_1 // 10
	number_2 = number_2 // 10

reversed_mass_3 = mass_3[::-1]

for item in reversed_mass_3:
	print(item, end='')