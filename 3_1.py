'''Python functions_1'''
#1 convert grams to ounces
def gr_to_oun(grams):
    ounches = 28.3495231 * grams
    return ounches
print(gr_to_oun(2))

#2 Fahrenheit to Celsium
def f_to_c(F):
    C = (5 / 9) * (F - 32)
    return C 
print(f_to_c(60))

#3 Chicken & Rabbits puzzle
def solve(numheads, numlegs):
    a=numheads*2 #если у каждой головы по 2 ноги
    b=numlegs-a #ног остается, распределяем их по кроликам
    rab=b/2 #кроликов
    chick=numheads-rab #куриц
    return (int(rab), int(chick))
print(solve(35,94))

#4 function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.
def primes(liss):
    new_liss=[]
    for i in range (0,len(liss)):
        is_prime=True
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
print(primes(mylist))

