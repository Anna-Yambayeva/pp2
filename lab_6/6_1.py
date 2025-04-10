#Python builtin functions exercises

#1 Write a Python program with builtin function to multiply all the numbers in a list
import math

def multiply_list(numbers):
    return math.prod(numbers)

if __name__ == "__main__":
    nums = [2, 3, 4, 5]
    result = multiply_list(nums)
    print("Список:", nums)
    print("Произведение всех чисел:", result)

#2 Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
def count_upper_lower(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

if __name__ == "__main__":
    test_string = input("Введите строку: ")
    upper_c, lower_c = count_upper_lower(test_string)
    print(f"Upper case letters: {upper_c}")
    print(f"Lower case letters: {lower_c}")

#3 Write a Python program with builtin function that checks whether a passed string is palindrome or not.
def is_palindrome(s):
    cleaned = "".join(s.split()).lower()
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    test_string = input("Введите строку: ")
    print("Является палиндромом?" , is_palindrome(test_string))

#4 Write a Python program that invoke square root function after specific milliseconds.
import time
import math

def delayed_sqrt(number, milliseconds):
    time.sleep(milliseconds / 1000.0)
    return math.sqrt(number)

if __name__ == "__main__":
    n = float(input("Enter a number to take square root of: "))
    ms = int(input("Enter milliseconds to wait: "))
    result = delayed_sqrt(n, ms)
    print(f"Square root of {n} after {ms} miliseconds is {result}")

#5 Write a Python program with builtin function that returns True if all elements of the tuple are true.
def all_true(tpl):
    return all(tpl)

if __name__ == "__main__":
    my_tuple = (1, True, "non-empty", 5) 
    print(all_true(my_tuple))  

    my_tuple2 = (1, 0, 2)      
    print(all_true(my_tuple2)) 