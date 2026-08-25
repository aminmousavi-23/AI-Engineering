# ------------------------------------------------------------
# 1. Comments
# ------------------------------------------------------------

# This is a single-line comment

"""
This is a multi-line string.

It can be used as a multi-line comment
when it is not assigned to a variable.
"""


# ------------------------------------------------------------
# 2. Numbers
# ------------------------------------------------------------

total = 10 + 11
print(total)

power = 10 ** 2
print(power)


# ------------------------------------------------------------
# 3. Strings
# ------------------------------------------------------------

my_long_string = """
This is a long string.
This is a long text.
"""

print(my_long_string)


# ------------------------------------------------------------
# 4. String Concatenation
# ------------------------------------------------------------

first_name = "Amin"
last_name = "Mousavi"

full_name = first_name + " " + last_name

print(full_name)


# ------------------------------------------------------------
# 5. String Length
# ------------------------------------------------------------

print(len(full_name))


# ------------------------------------------------------------
# 6. Boolean
# ------------------------------------------------------------

is_logged_in = False
is_admin = True

if is_logged_in == False:
    print("Please login to your account")
elif is_admin:
    print("Welcome our dear admin")
else:
    print("Welcome our dear user")


# ------------------------------------------------------------
# 7. Comparison Operators
# ------------------------------------------------------------

print(18 > 19)
print(18 < 19)
print(18 >= 19)
print(18 <= 19)
print(18 == 19)
print(18 != 19)


# ------------------------------------------------------------
# 8. Logical Operators
# ------------------------------------------------------------

# AND
print(18 > 19 and 18 < 19)

# OR
print(18 > 19 or 18 < 19)

# NOT
print(not 18 > 19)