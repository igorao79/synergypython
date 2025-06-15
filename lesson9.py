# 1

numbers = list(map(int, input().split()))
unique_numbers = set(numbers)
print(len(unique_numbers))

# 2

spisok1 = set(input().split())
spisok2 = set(input().split())

common_numbers = set(spisok1) & set(spisok2)
print(len(common_numbers))

# 3

numbers = list(map(int, input().split()))
seen = set()

for num in numbers:
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num)