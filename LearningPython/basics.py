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


# Strings
"""
- strings: single '' and double "" quotes
- can escape special characters by using opposite '/"
- \ can be used to escape the special character
- \n can be used for new line
- raw string: use r before string
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
"""
print('VARIABLES')
x = 2
for _ in range(5):
    print(_)
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
