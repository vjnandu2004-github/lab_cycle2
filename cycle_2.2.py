# Read a string containing numbers separated by space and convert it into an int list
print("ENTER LIST ELEMENTS")
str_list = list(map(int, input().split()))
print(str_list)

# Rotate the elements into kth position
k = int(input("enter k:"))
list_rotated = [(str_list[(i - k) % len(str_list)]) for i in range(len(str_list))]

# Removing duplicate elements
list_no_duplicates = list(set(list_rotated))

# Converting into a tuple
tpl1 = tuple(list_no_duplicates)
print(tpl1)

# Evaluation of function
list_no_duplicates.sort()
list_squared = [(x**2 - x) for x in list_no_duplicates]
print(list_squared)

# Merging the two lists into a single sorted list
list_final = sorted(list_squared + list_no_duplicates)
print(list_final)
