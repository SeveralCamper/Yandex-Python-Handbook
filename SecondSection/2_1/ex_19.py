product_name = input()
cost = int(input())
weight = int(input())
banknote = int(input())

product_str = f"{product_name}"
cost_str = f"{weight}кг * {cost}руб/кг"
weight_cost_str = f"{weight * cost}руб"
banknote_str = f"{banknote}руб"
change_str = f"{banknote - weight * cost}руб"

print("================Чек================")
print(f"Товар:{product_str:>29}")
print(f"Цена:{cost_str:>30}")
print(f"Итого:{weight_cost_str:>29}")
print(f"Внесено:{banknote_str:>27}")
print(f"Сдача:{change_str:>29}")
print("===================================")