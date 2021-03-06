"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""


"""
List Comprehensions
"""
odds = [1, 3, 5, 7, 9]
# like map
print([x+1 for x in odds])

# like filter
print([x for x in odds if 25 % x == 0])

# general form
# [<map expression> for <name> in <sequence expression> if <filter expression>]

"""
Dictionary Comprehensions
"""




# Write a list comprehension to produce the array [1, 2, 3, 4, 5]
# [num for num in range(0,50) if num % 3 == 0]
y = [num for num in range(1, 6)]

print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = [num**3 for num in range(1,10)]

print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = [word.upper() for word in a]

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?

# Two wasy to do this

y = [int(x) % 2 == 0 for x in x]

z = [x for x in x if int(x) % 2 == 0]

print(y)
print(z)