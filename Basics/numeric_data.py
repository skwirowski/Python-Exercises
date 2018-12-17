number_1 = 3
number_2 = 3.14

print(type(number_1))
print(type(number_2))

# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2
# Exponent:       3 ** 2
# Modulus:        3 % 2

# INCREMENTATION
num = 1
# 1
num = num + 1
print(num)
# 2
num += 1
print(num)
# 3
num *= 2
print(num)

# absolute value
print(abs(-10))
# round (second argument says we want to round to the first digit after the decimal)
print(round(3.75))
print(round(3.75, 1))

# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2

# CASTING - CASTS VALUES FROM STRINGS TO INTEGERS
num_1 = '100'
num_2 = '200'
print(num_1 + num_2)

num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)

