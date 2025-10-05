first_player = input()
second_player = input()
third_player = input()

if (first_player < second_player and first_player < third_player):
	print(first_player)
elif (second_player < first_player and second_player < third_player):
	print(second_player)
else:
	print(third_player)