print("Как Вас зовут?")
name = input()
print(f"Здравствуйте, {name}!\nКак дела?")
mood = input()
if (mood == "хорошо"):
	print("Я за Вас рада!")
elif (mood == "плохо"):
	print("Всё наладится!")