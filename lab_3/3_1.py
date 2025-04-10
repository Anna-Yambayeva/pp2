'''Python functions_1'''
#1 convert grams to ounces
print("convert grams to ounces:")
def gr_to_oun(grams):
    ounches = 28.3495231 * grams
    return ounches
print(gr_to_oun(2))
print("")

#2 Fahrenheit to Celsium
print("Fahrenheit to Celsium:")
def f_to_c(F):
    C = (5 / 9) * (F - 32)
    return C 
print(f_to_c(60))
print("")

#3 Chicken & Rabbits puzzle
print("Chicken & Rabbits puzzle:")
def solve(numheads, numlegs):
    a=numheads*2 #если у каждой головы по 2 ноги
    b=numlegs-a #ног остается, распределяем их по кроликам
    rab=b/2 #кроликов
    chick=numheads-rab #куриц
    return (int(rab), int(chick))
print(solve(35,94))
print("")

#4 function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.
print("Prime filter 1:")
def filter_prime(liss):
    new_liss=[]
    for i in range (0,len(liss)):
        is_prime=True
        if liss[i]==1:
            is_prime=False
        for j in range (2,int(liss[i] ** 0.5) + 1):
            if liss[i]<2:
                is_prime=False
                break
            if liss[i] % j == 0:
                is_prime=False
                break
        if is_prime:
            new_liss.append(liss[i])
    return(new_liss)

mylist=[1, 2, 3, 4, 5, 6, 7, 8, 9, 31]
print(filter_prime(mylist))
print("")

#4 same as previous, but using string
print("Prime filter 2:")
def prime(liss):
    liss=liss.split()
    for i in range (0,len(liss)):
        is_prime=True
        if int(liss[i])==1:
            is_prime=False
        for j in range (2,int(int(liss[i]) ** 0.5) + 1):
            if int(liss[i])<2:
                is_prime=False
                break
            if int(liss[i]) % j == 0:
                is_prime=False
                break
        if is_prime:
            print(liss[i],end=" ")
    return " "

list="1 2 3 4 5 6 7 8 9 31"
print(prime(list))
print("")

#5 function that accepts string from user and print all permutations of that string.
print("Permutations:")
def permutate(s,ans=""):
    if len(s)==0:
        print(ans)
        return ""
    for i in range (0,len(s)):
        a=s[i]
        s_a=s[:i]+s[i+1:]
        permutate(s_a, a+ans)

permutate("abc")
print("")

#6 function that accepts string from user, return a sentence with the words reversed
print("Reverse the string:")
def rev(s):
    s_list=[]
    s_list=s.split()
    s_list.reverse()
    return ' '.join(s_list)

print(rev("We are here"))
print("")

#7 Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
print("3 by 3:")
def has_33(nums):
    for i in range (0,len(nums)):
        if nums[i]==3:
            if (i>=1)and(i<=(len(nums)-2)):
                if (nums[i]==nums[i-1]):
                    return True
                if (nums[i]==nums[i+1]):
                    return True
    return False

nums=[1, 3, 3]
print(has_33(nums))
nums=[1, 3, 1, 3]
print(has_33(nums))
print("")

#8 Write a function that takes in a list of integers and returns True if it contains 007 in order
print("Spy game:")
def spy_game(nums):
    for i in range (0,len(nums)):
        if nums[i]==0:
            for j in range (i,len(nums)):
                if nums[j]==0:
                    for k in range (j,len(nums)):
                        if nums[k]==7:
                            return True
    return False

nums=[1,2,4,0,0,7,5]
print(spy_game(nums))
nums=[1,0,2,4,0,5,7]
print(spy_game(nums))
nums=[1,7,2,0,4,5,0]
print(spy_game(nums))
print("")

#9 function that computes the volume of a sphere given its radius.
print("Sphere volume:")
def sphere(r):
    V=(3/4)*(3.14)*r
    return V

print(sphere(1))
print("")

#10 function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.
print("Unique list:")
def unic(list):
    new_list=[]
    for i in range (0,len(list)):
        is_here=False
        for j in range(0,len(new_list)):
            if list[i]==new_list[j]:
                is_here=True
        if (not is_here):
            new_list.append(list[i])
    return new_list

list=["a", "a", "b", "b", "b", "c"]
print(unic(list))
print("")

#11 function that checks whether a word or phrase is palindrome or not
print("Palindrome:")
def palyndrom(slovo):
    if slovo == slovo[::-1]:
        print("yes")
        return ""
    print ("no")
    return ""

palyndrom("abba")
palyndrom("aab")
print("")

#12 functino histogram() that takes a list of integers and prints a histogram to the screen.
print("Histogram:")
def histogram(line):
    for i in range (0,len(line)):
        print("*"*int(line[i]))

line=[4, 9, 7]
histogram(line)
print("")

#13 program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20.
print("Guess the number - game:")
import random
def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    number_to_guess = random.randint(1, 20)
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    attempts = 0
    while True:
        print("\nTake a guess.")
        guess = int(input())
        attempts += 1
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break

guess_the_number()
