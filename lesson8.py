# 1

N = int(input())
numbers = [int(input()) for _ in range(N)]
reversed_numbers = numbers[::-1]
print(*reversed_numbers)


# 2

N = int(input())
arr = list(map(int, input().split()))
arr = [arr[-1]] + arr[:-1]
print(*arr)


# 3 

m = int(input())  
n = int(input()) 
weights = [int(input()) for _ in range(n)]  

weights.sort()  

i = 0           
j = n - 1       
boats = 0       

while i <= j:
    if weights[i] + weights[j] <= m:
        i += 1  
    j -= 1      
    boats += 1  

print(boats)
