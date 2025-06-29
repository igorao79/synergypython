# 1

def all_factorials(n):
    factorials = [1]  
    for i in range(1, n + 1):
        factorials.append(i * factorials[-1]) 
    return factorials[1:][::-1]

print(all_factorials(6))  


# 2

import collections

# Исходные данные
pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}

def get_suffix(age):
    """Функция для определения правильного склонения слова 'год'"""
    if age % 10 == 1 and age % 100 != 11:
        return 'год'
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        return 'года'
    else:
        return 'лет'

def get_pet(ID):
    """Получение информации о питомце по ID"""
    return pets.get(ID, False)

def create():
    """Добавление нового питомца в базу данных"""
    last = collections.deque(pets, maxlen=1)[0] if pets else 0
    new_id = last + 1
    
    name = input("Введите кличку питомца: ")
    pet_type = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner = input("Введите имя владельца: ")
    
    pets[new_id] = {
        name: {
            "Вид питомца": pet_type,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    }
    print(f"Питомец {name} успешно добавлен под ID {new_id}")

def read(ID):
    """Чтение информации о питомце"""
    pet_info = get_pet(ID)
    if not pet_info:
        print(f"Питомец с ID {ID} не найден")
        return
    
    name = list(pet_info.keys())[0]
    data = pet_info[name]
    age = data["Возраст питомца"]
    suffix = get_suffix(age)
    
    print(f'Это {data["Вид питомца"]} по кличке "{name}". '
          f'Возраст питомца: {age} {suffix}. '
          f'Имя владельца: {data["Имя владельца"]}')

def update(ID):
    """Обновление информации о питомце"""
    pet_info = get_pet(ID)
    if not pet_info:
        print(f"Питомец с ID {ID} не найден")
        return
    
    name = list(pet_info.keys())[0]
    print(f"Редактирование информации для питомца {name} (ID {ID})")
    
    pet_type = input(f"Вид питомца ({pet_info[name]['Вид питомца']}): ") or pet_info[name]['Вид питомца']
    age = input(f"Возраст питомца ({pet_info[name]['Возраст питомца']}): ") or pet_info[name]['Возраст питомца']
    owner = input(f"Имя владельца ({pet_info[name]['Имя владельца']}): ") or pet_info[name]['Имя владельца']
    
    pets[ID] = {
        name: {
            "Вид питомца": pet_type,
            "Возраст питомца": int(age),
            "Имя владельца": owner
        }
    }
    print("Информация обновлена")

def delete(ID):
    """Удаление питомца из базы данных"""
    if ID not in pets:
        print(f"Питомец с ID {ID} не найден")
        return
    
    name = list(pets[ID].keys())[0]
    del pets[ID]
    print(f"Питомец {name} (ID {ID}) удален из базы данных")

def pets_list():
    """Вывод списка всех питомцев"""
    if not pets:
        print("В базе данных нет питомцев")
        return
    
    print("\nСписок всех питомцев:")
    for pet_id, pet_info in pets.items():
        name = list(pet_info.keys())[0]
        data = pet_info[name]
        age = data["Возраст питомца"]
        suffix = get_suffix(age)
        
        print(f'ID {pet_id}: {data["Вид питомца"]} "{name}", '
              f'{age} {suffix}, владелец: {data["Имя владельца"]}')
    print()

def main():
    """Основная функция программы"""
    print("Добро пожаловать в систему учета питомцев ветеринарной клиники!")
    print("Доступные команды: create, read, update, delete, list, stop")
    
    while True:
        command = input("\nВведите команду: ").strip().lower()
        
        if command == 'stop':
            print("Работа программы завершена")
            break
            
        elif command == 'create':
            create()
            
        elif command == 'read':
            try:
                pet_id = int(input("Введите ID питомца: "))
                read(pet_id)
            except ValueError:
                print("Ошибка: ID должен быть числом")
                
        elif command == 'update':
            try:
                pet_id = int(input("Введите ID питомца: "))
                update(pet_id)
            except ValueError:
                print("Ошибка: ID должен быть числом")
                
        elif command == 'delete':
            try:
                pet_id = int(input("Введите ID питомца: "))
                delete(pet_id)
            except ValueError:
                print("Ошибка: ID должен быть числом")
                
        elif command == 'list':
            pets_list()
            
        else:
            print("Неизвестная команда. Попробуйте снова")

if __name__ == "__main__":
    main()