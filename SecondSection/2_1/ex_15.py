current_hours = int(input())
current_minutes = int(input())
delivery_time = int(input())

delivery_hours = delivery_time // 60
delivery_minutes = delivery_time % 60

final_hours = ((current_hours + delivery_hours) + (current_minutes + delivery_minutes) // 60) % 24
final_minutes = (current_minutes + delivery_minutes) % 60

if final_hours < 10:
	print(f'0{final_hours}:', end="")
else:
	print(f'{final_hours}:', end="")

if final_minutes < 10:
	print(f'0{final_minutes}', end="")
else:
	print(f'{final_minutes}', end="")