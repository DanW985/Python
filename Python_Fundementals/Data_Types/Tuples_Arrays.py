#arrays
from array import array

a1 = array('l') #l is of type integer so the array will be of integers
a2 = array('l', [10,20,30,100,200,300])
a3 = array('u', 'Hello') #u is of type unicode so the array will be of characters
a4 = array('d', [3.1459, 2.71828, 1.41421, 1.61803]) #d is of type decimal so the array will be of decimals(floating point)

print(f'Before pop: {a2}')
a2.pop() #pop removes the last element from the array
print(f'After pop: {a2}')

a3.append('!')
print(f'{a3}')
a3.insert(5, '?')
print(f'{a3}')

print('a4[0]: ' + str(a4[0]))

print()

#Tuples - sequence of elements that cannot be modified once created in the programme
t1 = (1,2,3)
t2 = (3.1459, 2.71828, 1.41421, 1.61803)
t3 = ('Hello', 'World')
t4 = ('!')

print(f't1: {t1}')
print(f't2[0]: {t2[0]}')
print('t3 + t4: {}'.format(t1 +t2))