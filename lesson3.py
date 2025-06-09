# № 1
def get_pet_info():
    """Запрашивает и проверяет данные о питомце"""
    while True:
        pet_type = input("Введите вид питомца: ").strip()
        if pet_type.replace(' ', '').isalpha():
            break
        print("Ошибка: вид питомца должен содержать только буквы и пробелы")

    while True:
        pet_age = input("Введите возраст питомца: ").strip()
        if pet_age.isdigit() and int(pet_age) > 0:
            pet_age = int(pet_age)
            break
        print("Ошибка: возраст должен быть положительным числом")

    while True:
        pet_name = input("Введите кличку питомца: ").strip()
        if pet_name:
            break
        print("Ошибка: кличка не может быть пустой")

    return pet_type, pet_age, pet_name

def format_age(age):
    """Форматирует возраст с правильным склонением"""
    if age % 100 in (11, 12, 13, 14):
        return f"{age} лет"
    elif age % 10 == 1:
        return f"{age} год"
    elif age % 10 in (2, 3, 4):
        return f"{age} года"
    else:
        return f"{age} лет"

def main():
    pet_type, pet_age, pet_name = get_pet_info()
    
    formatted_age = format_age(pet_age)
    print(f'\nЭто {pet_type.lower()} по кличке "{pet_name.capitalize()}". Возраст: {formatted_age}.')

if __name__ == "__main__":
    main()



# 2
stage1 = input("1-й этап развития человека: ")
stage2 = input("2-й этап развития человека: ")
stage3 = input("3-й этап развития человека: ")
stage4 = input("4-й этап развития человека: ")
stage5 = input("5-й этап развития человека (Homo sapiens sapiens): ")

# Выводим этапы с разделителем
print(stage1, stage2, stage3, stage4, stage5, sep=' => ')