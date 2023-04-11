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