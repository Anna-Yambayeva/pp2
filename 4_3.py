#Python iterators and generators

#1 Create a generator that generates the squares of numbers up to some number N.
def squares(n):
    for num in range(1, n + 1):
        yield num ** 2  

N = int(input("Введите число до которого будут выводиться квадраты чисел, начиная с 1: "))
squares_list = list(squares(N))
print(squares_list)

#2 Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def even_numbers(n):
    for num in range(2, n, 2):
        yield num

n = int(input("Введите число: "))
even_str = ", ".join(str(num) for num in even_numbers(n))
print(even_str)

#3 Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def div_by3n4(n):
    for divided in range(0, n + 1):
        if (divided % 4 == 0 and divided % 3 == 0):
            yield divided

n = int(input("Введите число: "))
print(list(div_by3n4(n)))

#4 Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2

a = int(input("Введите начальное число: "))
b = int(input("Введите последнее число: "))
print(f"Квадраты чисел от {a} до {b}:")
for square in squares(a, b):
    print(square)

#5 Implement a generator that returns all numbers from (n) down to 0.
def to_zero(n):
    for nums in range(n, -1, -1):
        yield nums

n = int(input("Введите число: "))

for num in to_zero(n):
    print(num)