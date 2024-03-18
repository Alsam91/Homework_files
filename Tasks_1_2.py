# Задание 1
def cook_book_dict(file_name):
    cook_book = {}
    with open(file_name, encoding="utf-8") as file:
        for line in file:
            dish_name = line.strip()
            ingredients_count = int(file.readline().strip())
            ingredients = []
            for i in range(ingredients_count):
                ingredient_name, quantity, measure = file.readline().strip().split(" | ")
                ingredients.append({"ingredient_name": ingredient_name, "quantity": quantity, "measure": measure})
            file.readline()
            cook_book[dish_name] = ingredients
    return cook_book


print(cook_book_dict("recipes.txt"))


# Задание 2
def get_shop_list_by_dishes(dishes, person_count):
    cook_book = cook_book_dict("recipes.txt")
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = dict(ingredient)
            new_shop_list_item["quantity"] = int(new_shop_list_item["quantity"]) * person_count
            if new_shop_list_item["ingredient_name"] not in shop_list:
                shop_list[new_shop_list_item["ingredient_name"]] = new_shop_list_item
            else:
                shop_list[new_shop_list_item["ingredient_name"]]["quantity"] += new_shop_list_item["quantity"]
    return shop_list


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
