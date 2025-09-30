child_name = input()
info = int(input())
info_dump = info

digits = []

while info > 0:
	digit = int(info % 10)
	digits.append(digit)
	info = info / 10

print(f"Группа №{digits[2]}.")
print(f"{digits[0]}. {child_name}.")
print(f"Шкафчик: {info_dump}.")
print(f"Кроватка: {digits[1]}.")