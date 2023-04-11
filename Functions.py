# Function is a block of code that performs a particular task; function is specified with the 'def' keyword

# Function creation
def greetings_function(name, age):
    print('Welcome '+name+ '. You are', age, 'years old')

# Function call
greetings_function('Faith', 20)

# Function creation to greet just one user in a list/tuple containing many users
def greetings_function(*names):
    print('Welcome', names[1])

# Function call
greetings_function('Faith', 'Tim', 'Tom')

# Taking input from the user
def greetings_function(name,age):
    print('Welcome'+name+'. You are', age, 'years old')

# Assigining the input function to the variables and calling the function
name = input('Enter your name: ')
age = input('Enter your age: ')
greetings_function(name,age)
