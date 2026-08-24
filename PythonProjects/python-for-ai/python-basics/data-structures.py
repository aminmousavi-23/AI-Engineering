# ============================================================
# Data Structures
# ============================================================


# ------------------------------------------------------------
# 1. Lists - Creating Lists
# ------------------------------------------------------------

# Empty list
my_list = []

# List with items
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, True, 3.14]  # Different types are OK


# ------------------------------------------------------------
# 2. Lists - Accessing Items
# ------------------------------------------------------------

fruits = ["apple", "banana", "orange"]

print(fruits[0])     # "apple"
print(fruits[1])     # "banana"
print(fruits[-1])    # "orange"
print(fruits[-2])    # "banana"


# ------------------------------------------------------------
# 3. Lists - Slicing
# ------------------------------------------------------------

print(fruits[0:2])   # ["apple", "banana"]
print(fruits[1:])    # ["banana", "orange"]


# ------------------------------------------------------------
# 4. Lists - Changing Items
# ------------------------------------------------------------

fruits[0] = "mango"
print(fruits)


# ------------------------------------------------------------
# 5. Lists - Adding Items
# ------------------------------------------------------------

fruits.append("grape")      # Add to end
fruits.insert(1, "kiwi")    # Insert at position


# ------------------------------------------------------------
# 6. Lists - Removing Items
# ------------------------------------------------------------

fruits.remove("banana")     # Remove by value

last = fruits.pop()         # Remove and return last

del fruits[0]               # Remove by index


# ------------------------------------------------------------
# 7. Lists - Information
# ------------------------------------------------------------

numbers = [3, 1, 4, 1, 5, 9]

print(len(numbers))         # 6
print(numbers.count(1))     # 2
print(numbers.index(4))     # 2


# ------------------------------------------------------------
# 8. Lists - Sorting
# ------------------------------------------------------------

numbers.sort()
print(numbers)              # [1, 1, 3, 4, 5, 9]

numbers.reverse()
print(numbers)              # [9, 5, 4, 3, 1, 1]


# ------------------------------------------------------------
# 9. Lists - Copying
# ------------------------------------------------------------

new_list = numbers.copy()


# ------------------------------------------------------------
# 10. Lists - Checking Items
# ------------------------------------------------------------

fruits = ["apple", "banana", "orange"]

if "apple" in fruits:
    print("Found apple!")


# ------------------------------------------------------------
# 11. Lists - Checking if Empty
# ------------------------------------------------------------

if fruits:
    print("List has items")
else:
    print("List is empty")


# ------------------------------------------------------------
# 12. Lists - Modifying During a Loop
# ------------------------------------------------------------

# Dangerous - don't modify a list while iterating over it
numbers = [1, 2, 3, 4]

for num in numbers:
    if num == 2:
        numbers.remove(num)


# Better - use list comprehension
numbers = [num for num in numbers if num != 2]


# ------------------------------------------------------------
# 13. Lists - References vs Copies
# ------------------------------------------------------------

# Wrong - both variables point to the same list
list1 = [1, 2, 3]
list2 = list1

list2.append(4)

print(list1)               # [1, 2, 3, 4]


# Right - make a copy
list1 = [1, 2, 3]
list2 = list1.copy()

list2.append(4)

print(list1)               # [1, 2, 3]


# ============================================================
# Dictionaries
# ============================================================
