'''Python Operators'''
#Operators are used to perform operations on variables and values
print(10 + 5)

'''Python divides the operators in the following groups:
Arithmetic operators (+ - * / % ** //)
Assignment operators (= += -= *= /= %= //= &= |= ^= >>= <<= :=)
Comparison operators (== != > < >= <=)
Logical operators (and or not)
Identity operators (is is not)
Membership operators (in not in)
Bitwise operators (& | ^ ~ << >>)
'''

x=2
y=3
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)
print(x//y)



print(" ")
a=5
print(a)

a+=3
print(a)

a-=3
print(a)

a*=3
print(a)

a/=3
print(a)

a%=3
print(a)

a//=3
print(a)

a**3
print(a)

a=5

a&=3
print(a)

a|=3
print(a)

a^=3
print(a)

a>>=3
print(a)

a<<=3
print(a)


print(" ")
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x<=y)
print(x>=y)



print(" ")
x=1 
y=0
print((x<5)and(x<10))
print((x<5)or(x<0))
print(not((x<5)and(x<10)))



print(" ")
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True because z is the same object as x

print(x is y)
# returns False because x is not the same object as y, even if they have the same content

print(x is not z)
# returns False because z is the same object as x

print(x is not y)
# returns True because x is not the same object as y, even if they have the same content

print(" ")
x = ["apple", "banana"]

print("banana" in x)
print("pineapple" not in x)



print(" ")
print(6 & 3)
'''
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:
6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
'''

print(6 | 3)
'''
The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111
'''

print(6 ^ 3)
'''
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
'''

print(~3)
'''
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100
'''

print(3 << 2)
'''
The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100
'''

print(8 >> 2)
'''
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010
'''

'''Operator precedence describes the order in which operations are performed. 
()	Parentheses	
**	Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	Addition and subtraction	
<<  >>	Bitwise left and right shifts	
&	Bitwise AND	
^	Bitwise XOR	
|	Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators
not	Logical NOT	
and	AND	
or	OR'''

print(4 or 5 + 10 or 8)
print(1 or 2 and 3)
print(5 == 4 + 1)
print(5 + 4 - 7 + 3)
print(not 5 == 5)
print(100 + ~3)
print(100 - 3 ** 3)

