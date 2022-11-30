# задача 3
# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод

import random

print("Введите длинну списка")
n = int (input())
list1 = list(range(1,n+1))
print(list1)

for i in list1 : 
    i = random.sample(list1, n)
    
print(i)