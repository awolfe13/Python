# following Telusko python videos on youtube

# Mathematics
"""
- order of operations same
- the + - * all work the same (output is integer)
- however divide / creates a double output
- use double // for integer
- % is modular (gets the remainder
"""

print('MATHEMATICS')
print(10 + 2)
print(10 - 3)
print(2 * 4)
print(10 / 5)
print(10 // 5)
print(10 % 3)
print('')

#Data Types
"""
- use type( var ) to see data type
- types: None, Numeric, List, Tuple, Set, String, Range, Dictionary
- None: you have a variable assigned without any value (similar to null)
- Numeric: Int (3), float (2.5) , complex (6+9j) , bool (1, 0)
    - complex: (a+bi) -> (a+bj) have to replace i with j (imaginary number)
    - j represented square root of minus 1
"""

print('GET DATA TYPES')
name = 'ariel'
print(type(name))
print('')


# Conversions
"""
- int ( ) converts into integer
- float ( ) converts to float
- complex (b,j) converts to complex
"""

print('CONVERSIONS')
a = 5.6
b = int(a)
print(b)
print(float(b))
j = 10
print(complex(b,j))
print(int(True))
print(int(False))
print('')

# Strings
"""
- strings: single '' and double "" quotes
- can escape special characters by using opposite '/"
- \ can be used to escape the special character
- \n can be used for new line
- raw string: use r before string
- single character is still a string, there is no char 
"""

print('STRINGS')
print("Ariel's laptop")
print('Ariel has a "laptop"')
print('Ariel\'s "laptop"')
print('Ariel ' * 3)
print(r'This prints newline \n without executing it')
print('')

# String Variables
"""
- strings are arrays
- strings are IMMUTABLE
- len( ) finds length of string
"""
print('STRING VARIABLES')
name = 'Ariel'
print(name + ' rocks')

print(name[0])
# if using -1 for index, it will go from right to left (no 0, starts at -1)
print(name[-1])
# can select a range (starting index : ending index)
print(name[0:2])
# dont specify ending - will go to the end
print(name[2:])
# dont specify beginning - will start at beginning and end at the end given
print(name[:3])
# CANNOT reassign value
# name[0] = 'T'
# how to change
print('B' + name[1:])
# len() length of string
print(len(name))
print('')


# Variables
"""
- the single underscore _ represents output of previous operation
- variables have <address>  (variables 'tag' the same value)
- use id( var ) or id ( value ) to get the address
- if the var VALUE is the same, both variables will point to the same variable
- garbage collection: value no longer being 'tagged' (data in memory)
"""
print('VARIABLES')
x = 2
y = x
print(id(x))
print(id(y))
print(id(2))
x = 3
print(id(x))

for _ in range(5):
    print(_)
print('')

#CONTS
"""
- consts use capital letters
- but no physical restraints from changing const values
"""
print('CONSTS')
CONST = 100
CONST = 99
print(CONST)
print('')


# Lists (aka arrays)
"""
- can have different data types in SAME array
- can have a list of lists
- lists are MUTABLE
- lists use []
"""

print('LISTS aka ARRAYS')

nums = [0, 1, 2, 3, 4]
print(nums)
print(nums[0])
print(nums[2:4])
print(nums[-1])

#append (value) to the end
nums.append(5)
print(nums)

#insert with (index, value)
nums.insert(0, 12)
print(nums)

#remove (value)
nums.remove(12)
print(nums)

#pop (index)
nums.pop(5)
print(nums)

#pop with no index
nums.pop()
print(nums)

#delete multiple values [index]
del nums[2:]
print(nums)

#extends add multiple values []
nums.extend([88, 14, 55])
print(nums)

#min, max, sum
print(min(nums))
print(max(nums))
print(sum(nums))

#sort
nums.sort()
print(nums)

names = ['Ariel', 'Nancy', 'Julia']

# can have different data types in same array
values = [9.5, 'python', 7]
print(values)

# can have a list of lists
listOfLists = [nums, names]
print(listOfLists)
print('')

#Tuple
"""
- list that is IMMUTABLE
- use ()
- can type typle  then . and see available functions
- creation is FASTER than lists
"""

print('TUPLES')
tuple = (12, 53, 93)
print(tuple)
# immutable - cannot change
# tuple[0] = 1
print('')

#Set
"""
- does not follow the sequence (is randomized so no indexing)
- use {}
- does not display duplicates
"""

print('SET')
set = {43, 77, 23, 77}
print(set)
print('')

#Range
"""
- define a range with range ( start, end, iteration )
   range(10) -> starts at 0, through 10
   range(5,10) -> starts at 5, through 10
   range(2,10,2) -> starts at 2, through 10, skips 2
- can convert range to list (or use for loop) to view actual values in range
"""

print('RANGE')
print(range(10))
print(list(range(10)))
print(range(5,10))
print(list(range(5,10)))
print(range(2,10,2))
print(list(range(2,10,2)))
print('')

#Dictionary
"""
- its associative array instead of numeric index key => value
- key needs to be unique 
- d = {'ariel': 'android', 'loser': 'iphone' }
    - defined by curly brackets (same as set, no repeating keys)
- d.keys(), d.values()
- d[key] is the same as d.get(key)
"""

print('DICTIONARY')
dict = {'ariel': 'android', 'loser': 'iphone'}
print(dict)
print(dict.keys())
print(dict.values())
print(dict['ariel'])
print(dict.get('loser'))
print('')


#Operators
"""
- Arithmetic (+,-,/,*)
    - arithmetic shortcut: x += 2 (x = x + 2), x *= 3, etc
- Assignment (=)
    - assignment shortcut: a,b = 5,6  (instead of a = 5, b = 6)
- Relational (<, >, ==, !=)
- Logical (and, or, not)
- Unary (-)
    - negative - to positive or vice versa
"""

print('OPERATORS')
unary = 8
print(unary)
unary = -unary
print(unary)
a = 1
b = 'ariel'
print(a == 1 and b != 'loser')
x = True
print(not x)
x = not x
print(x)
print('')


#Number Systems
"""
- decimal: base 10, 0-9
- binary: base 2, 0-1
- octal: base 8, 0-7
- hexadecimal: base 16, [0-9, a-f]
- decimal -> binary use bin() -> 0b#### binary format
    -reverse: 0b101 -> 5
- decimal -> octal use oct( ) -> 0o####
    -reverse 0x31
- decimal -> hex use hex( ) -> 0x###
    reverse: 0xf -> 15
"""

print('NUMBER SYSTEMS')
print(bin(25))
print(0b101)
print(oct(25))
print(0o31)
print(hex(10))
print(0xf)
print('')


#Swap Variables
"""
- instead of using a temp variable, can use this formula
    a = a + b
    b = a - b
    a = a - b
- use xor is the ^ to save bits
    a = a ^ b
    b = a ^ b
    a = a ^ b
- double assignment    
    a,b = b,a
    -has a stack order, assigns a = b, then b = a
"""

a = 2
b = 78
a = a + b #80
b = a - b #2
a = a - b #78
print(a)
print(b)

a = 5
b = 10
a = a ^ b #80
b = a ^ b #2
a = a ^ b #78
print(a)
print(b)

a = 33
b = 66
a,b = b,a
print(a)
print(b)
print('')


#BitWise Operators
"""
- Complement (~)
    - reverse the binary: 0 -> and 1 -> so 001100 -> 110011
    - dont store negative numbers in memory, so have to store as a positive number
    - ~12 -> -13
- And (&)
    12 & 13
    -comparing the binary together, so 0 & 0 = 0, 1 & 0 = 0
    -comparing 12 binary vertical to 13 binary
    12 binary: 00001100
    13 binary: 00001101
               00001100 -> which is 12
- Or (|)
    20 | 10
    -comparing the binary together, so 0 | 0 = 0, 1 | 0 = 1
    -comparing 20 binary vertical to 10 binary
    20 binary: 00010100
    10 binary: 00001010
               00011110 -> 30
- XOR (^)
    0 0 -> 0    0 1 -> 1    1 0 -> 1    1 1 -> 0
    15 ^ 3
    12 binary: 00001100
    13 binary: 00001101
               00000001
- Left Shift (<<)
    -gaining bits
    10 << 2
    10 binary: 00001010
                       00
                 00101000 -> 40
- Right Shift (>>)
   -losing bits
   10 >> 2
   10 binary:  00001010
             00000010 -> 2
"""

print('BITWISE OPERATORS')
print(~12)
print(~10)
print(12 & 13)
print(20|10)
print(12 ^ 13)
print(10 << 2)
print(0b101000)
print(10 >> 2)
print(0b10)



