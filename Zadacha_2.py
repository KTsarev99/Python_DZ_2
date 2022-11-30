# задача 2

n = int (input())

for i in (range(1, (n)+1)) :
    print((1 + 1/i)**i)

sum = 0
for g in (range(1, (n)+1)) :
    sum = sum + (1 + 1/i)**i
print(sum)