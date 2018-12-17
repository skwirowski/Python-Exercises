my_message = 'Hello World'
multiple_lines_message = """Hello World! Hello World! Hello World!
Hello World! Hello World! Hello World!"""

print(my_message)
print(multiple_lines_message)

# Get length of the string
print(len(my_message))
# Get specific index character from string (indexes start from 0)
print(my_message[0])
# SLICING
# First index is inclusive and last one is not
print(my_message[0:5])
# Leaving first value (index) empty means "start from the beginning"
print(my_message[:5])
# Leaving last value (index) empty means "go all the way to the end"
print(my_message[6:])

# Lower/Upper Case
print(my_message.lower())
print(my_message.upper())

# Count specific characters in the string
print(my_message.count('l'))
# Find index where certain characters can be found (if character doesn't exist returns -1)
print(my_message.find('World'))

# Replace some characters in our string with some other characters
# 1 - creating new variable
my_new_message = my_message.replace('World', 'Universe')
print(my_new_message)
# 2 - setting the same variable again
my_message = my_message.replace('World', 'Universe')
print(my_message)

# STRINGS CONCATENATIONS
greeting = 'Hello'
name = 'Paul'
# 1
message = greeting + ', ' + name + '. Welcome!'
print(message)
# 2
message = '{}, {}. Welcome!!'.format(greeting, name)
print(message)
# 3 - F strings
message = f'{greeting}, {name.upper()}. Welcome!!!'
print(message)

# DIR - it shows us all of the attributes and methods that we have access to with variable we passed as an argument
print(dir(name))
print(help(str))
print(help(str.lower))
