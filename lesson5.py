# 1 

num = input("Введите число: ")

try:
    num = int(num)
    
    if num > 0:
        if num % 2 == 0:
            print(f"Число {num} положительное и четное")
        else:
            print(f"Число {num} положительное и нечетное")
    elif num < 0:
        if num % 2 == 0:
            print(f"Число {num} отрицательное и четное")
        else:
            print(f"Число {num} отрицательное и нечетное")
    else:  # num == 0
        print("Число равно 0")
except ValueError:
    print("Вы ввели не число")


# 2 

word = input("Введите слово из маленьких латинских букв: ")

vowels = ['a', 'e', 'i', 'o', 'u']
vowel_counts = {v: 0 for v in vowels}
consonants_count = 0

for char in word:
    if char in vowels:
        vowel_counts[char] += 1
    else:
        consonants_count += 1

total_vowels = sum(vowel_counts.values())

print(f"Гласных букв: {total_vowels}")
print(f"Согласных букв: {consonants_count}")

for v in vowels:
    if vowel_counts[v] == 0:
        print(False)
    else:
        print(f"Количество буквы '{v}': {vowel_counts[v]}")



# 3

try:
    sum_required = int(input("Введите минимальную сумму инвестиций: "))
    mike = int(input("Введите сумму инвестиций Майкла: "))
    ivan = int(input("Введите сумму инвестиций Ивана: "))

    if mike >= sum_required and ivan >= sum_required:
        print(2)
    elif mike >= sum_required:
        print("Mike")
    elif ivan >= sum_required:
        print("Ivan")
    elif mike + ivan >= sum_required:
        print(1)
    else:
        print(0)

except ValueError:
    print("Ошибка: введите корректные числовые значения.")




