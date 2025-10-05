petr_speed = int(input())
vasily_speed = int(input())
anatoly_speed = int(input())

winers = []

if (petr_speed > anatoly_speed and petr_speed > vasily_speed):
	winers.append("Петя")
	if (anatoly_speed > vasily_speed):
		winers.append("Толя")
		winers.append("Вася")
	else:
		winers.append("Вася")
		winers.append("Толя")
elif (vasily_speed > petr_speed and vasily_speed > anatoly_speed):
	winers.append("Вася")
	if (anatoly_speed > petr_speed):
		winers.append("Толя")
		winers.append("Петя")
	else:
		winers.append("Петя")
		winers.append("Толя")
elif (anatoly_speed > vasily_speed and anatoly_speed > petr_speed):
	winers.append("Толя")
	if (petr_speed > vasily_speed):
		winers.append("Петя")
		winers.append("Вася")
	else:
		winers.append("Вася")
		winers.append("Петя")

i = 1
for item in winers:
	print(f"{i}. {item}")
	i += 1