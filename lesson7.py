# 1

slovo = input("Введите одно слово: ").strip()

if " " in slovo:
    print("Ошибка: введите только одно слово без пробелов.")
elif slovo == "":
    print("Ошибка: вы ничего не ввели.")
elif slovo == slovo[::-1]:
    print("yes")
else:
    print("no")


# 2

s = input()
result = ' '.join(s.split())
print(result)
