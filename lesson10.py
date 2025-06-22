# 1

pets = {}


pet_name = input("Введите имя питомца: ")
pet_type = input("Введите вид питомца: ")
pet_age = int(input("Введите возраст питомца: "))
owner_name = input("Введите имя владельца: ")


pets[pet_name] = {
    'Вид питомца': pet_type,
    'Возраст питомца': pet_age,
    'Имя владельца': owner_name
}


if 11 <= pet_age % 100 <= 14:
    age_suffix = "лет"
else:
    if pet_age % 10 == 1:
        age_suffix = "год"
    elif pet_age % 10 in [2, 3, 4]:
        age_suffix = "года"
    else:
        age_suffix = "лет"


pet_info = f"Это {pets[pet_name]['Вид питомца']} по кличке \"{pet_name}\". Возраст питомца: {pet_age} {age_suffix}. Имя владельца: {pets[pet_name]['Имя владельца']}."


print(pet_info)


# 2 

my_dict = {}

for num in range(10, -6, -1):  
    my_dict[num] = num ** num

print(my_dict)