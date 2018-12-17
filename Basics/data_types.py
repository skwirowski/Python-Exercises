# LISTS ###########
courses = ['History', 'Physics', 'Biology', 'English']
nums = [1, 4, 6, 2, 5, 3, 7, 9, 8]

# Getting first index
print(courses[0])
# Getting last index
print(courses[-1])
# Getting one before last index
print(courses[-2])

# ADDING ITEMS TO THE LIST
# Append - adds to the end of the list
courses.append('Art')
print(courses)
# Insert - adds to the specific location in our list (first argument is location of adding element)
courses.insert(0, 'Science')
print(courses)
# Extend - adds multiple values to the end of our list
courses_2 = ['Math', 'Sports']
courses.extend(courses_2)
print(courses)

# REMOVING ITEMS FROM THE LIST
# Remove - removes item from the list
courses.remove('Math')
print(courses)
# Pop - removes last element from the list (it grabs value that was popped of the list
courses.pop()
popped = courses.pop()
print(courses)
print(popped)

# SORTING LISTS
# Reverse list
courses.reverse()
print(courses)
# Sort list in alphabetical order
courses.sort()
print(courses)
# Sort list in ascending order
nums.sort()
print(nums)
# Sort list in reversed to alphabetical/ascending order
courses.sort(reverse=True)
nums.sort(reverse=True)
print(courses)
print(nums)
# Get sorted version of list item without altering the original list
sorted_courses





