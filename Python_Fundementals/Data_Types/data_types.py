"""
order of operations: (PEDMAS)
() (Parentheses)
** Exponent
~ + - (unary operations)
* / % // (Division, Multiplication)
+ - (Addition, Subtraction)
>> << (shift bitwise)
& (AND bitwise)
^ | (NOT, OR bitwise)
<= < > >= (comparison)
<> == != (equality)
= %= /= //= -= += *= **= (assignment)

"""

amount = 163400
time = 57.5

rate = amount / time
print('Rate: ' + str(rate)) #when printing integers you need to convert to a string using str())

bits = 16
size = 2 ** 16
print('size: ' + str(size))

print('11 // 3: ' +str(11 // 3)) #integer division
print('11 / 3: ' + str(11 / 3)) #float division
print('11 % 3: ' + str(11 % 3)) #modulus = remainder
#print('11 / 0: ' + str(11 / 0)) #divsion by zero! error!

#PEDMAS
print (10 -2 ** 2 / 2 +5)