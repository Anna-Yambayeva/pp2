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
