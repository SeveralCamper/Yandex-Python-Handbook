petr_speed = int(input())
vasily_speed = int(input())
anatoly_speed = int(input())

if (petr_speed > vasily_speed and petr_speed > anatoly_speed):
	print("Петя")
elif (vasily_speed > petr_speed and vasily_speed > anatoly_speed):
	print("Вася")
elif (anatoly_speed > vasily_speed and anatoly_speed > petr_speed):
	print("Толя")