# № 1

try:
    a = float(input("Введите первую сторону прямоугольника: "))
    b = float(input("Введите вторую сторону прямоугольника: "))
    
    area = a * b
    perimeter = 2 * (a + b)

    area_rounded = round(area, 2)
    perimeter_rounded = round(perimeter, 2)

    if area_rounded.is_integer():
        area_rounded = int(area_rounded)  
    if perimeter_rounded.is_integer():
        perimeter_rounded = int(perimeter_rounded)

    print(f"Площадь прямоугольника равна {area_rounded}")
    print(f"Периметр прямоугольника равен {perimeter_rounded}")

except ValueError:
    print("Ошибка: Введите действительные числа.")



# № 2

input_str = input("Введите пятизначное число: ")

try:
    num = int(input_str)
    
    if num < 10000 or num > 99999:
        print("Ошибка: Введите пятизначное число.")
    else:
        # Извлекаем цифры числа
        ten_thousands = num // 10000
        thousands = (num // 1000) % 10
        hundreds = (num // 100) % 10
        tens = (num // 10) % 10
        ones = num % 10

        result = (tens ** ones) * hundreds / (ten_thousands - thousands)

        print(f"Результат: {result}")

except ValueError:
    print("Ошибка: Введите целое число.")
