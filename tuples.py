# Tuples are used to store multiple items in a variable. Tuples are immutable; they allow 
# the repetiiton of the same values, they allow various data types. Tuples are useful when one is
# working on co-ordinates, values you dont want to change e.t.c

# Construct a tuple
three_numbers = tuple((1, True, 'home'))

three_numbers = (1,2,3,'home',1, True)
strings = ('land', 'home', 'earth')
boo = (True, False, True)
print(three_numbers)

# To find the number of values in a tuple
print(len(three_numbers))

# To find the type of a tuple
print(type(three_numbers))

# To find the data type of a specific tuple
print(type(three_numbers[0]))
