# # 1

N = int(input("Введите количество чисел: "))

count_zeros = 0

print(f"Введите {N} целых чисел:")

for _ in range(N):
    num = int(input())
    if num == 0:
        count_zeros += 1

print("Количество нулей:", count_zeros)

# # 2


X = int(input("Введите натуральное число X: "))
count = 0

sqrt_X = int(X ** 0.5)

for i in range(1, sqrt_X + 1):
    if X % i == 0:
        if i == X // i:
            count += 1 
        else:
            count += 2 

print("Количество делителей:", count)


# 3


A = int(input())
B = int(input())

for i in range(A, B + 1):
    if i % 2 == 0:
        print(i, end=' ')


