# ============================================================
# Functions
# ============================================================


# ============================================================
# 1. Creating and Calling Functions
# ============================================================


# ------------------------------------------------------------
# 1.1 Creating a Function
# ------------------------------------------------------------

def greet():
    print("Hello, world!")
    print("Welcome to Python!")


# ------------------------------------------------------------
# 1.2 Calling a Function
# ------------------------------------------------------------

greet()


# ------------------------------------------------------------
# 1.3 Empty Function with pass
# ------------------------------------------------------------

def function_name():
    # Code goes here
    # Must be indented
    pass


# ============================================================
# 2. Function Naming
# ============================================================


# ------------------------------------------------------------
# 2.1 Good Function Names
# ------------------------------------------------------------

def calculate_total():
    pass


def send_email():
    pass


def validate_password():
    pass


# ------------------------------------------------------------
# 2.2 Bad Function Names
# ------------------------------------------------------------

def func1():                    # Not descriptive
    pass


def Calculate():                # Should be lowercase
    pass


# ============================================================
# 3. Calling Functions Multiple Times
# ============================================================

def say_goodbye():
    print("Goodbye!")
    print("See you later!")


say_goodbye()
say_goodbye()
say_goodbye()


# ============================================================
# 4. Functions with Logic
# ============================================================

def check_weather():
    temperature = 25

    if temperature > 30:
        print("It's hot!")
    else:
        print("Nice weather!")


check_weather()


# ============================================================
# 5. Parameters and Arguments
# ============================================================


# ------------------------------------------------------------
# 5.1 Why Use Parameters?
# ------------------------------------------------------------

# Without parameters - inflexible

def greet_alice():
    print("Hello, Alice!")


# With parameters - flexible

def greet(name):
    print(f"Hello, {name}!")


greet("Alice")
greet("Bob")
greet("Charlie")


# ------------------------------------------------------------
# 5.2 Multiple Parameters
# ------------------------------------------------------------

def introduce(name, age):
    print(f"My name is {name}")
    print(f"I am {age} years old")


introduce("Alice", 25)
introduce("Bob", 30)


# ------------------------------------------------------------
# 5.3 Multiple Parameters - Order Matters
# ------------------------------------------------------------

def calculate_total(price, tax_rate, discount):
    tax = price * tax_rate
    final_price = price + tax - discount

    print(f"Total: ${final_price}")


calculate_total(100, 0.08, 10)      # $98


# ============================================================
# 6. Default Parameters
# ============================================================

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


# Use default value

greet("Alice")                      # Hello, Alice!


# Override default value

greet("Bob", "Hi")                  # Hi, Bob!
greet("Charlie", "Hey")             # Hey, Charlie!


# ============================================================
# 7. Positional and Keyword Arguments
# ============================================================


# ------------------------------------------------------------
# 7.1 Positional Arguments
# ------------------------------------------------------------

def create_profile(name, age, city):
    print(f"{name}, {age}, from {city}")


# Order matters

create_profile("Alice", 25, "NYC")


# ------------------------------------------------------------
# 7.2 Keyword Arguments
# ------------------------------------------------------------

# Order does not matter

create_profile(
    city="NYC",
    age=25,
    name="Alice"
)

create_profile(
    name="Bob",
    city="LA",
    age=30
)


# ============================================================
# 8. Argument Errors
# ============================================================

def greet_person(name, age):
    print(f"Hi {name}, you're {age}")


# Wrong - too few arguments

# greet_person("Alice")
# TypeError


# Wrong - too many arguments

# greet_person("Alice", 25, "NYC")
# TypeError


# Right

greet_person("Alice", 25)


# ============================================================
# 9. Return Values
# ============================================================


# ------------------------------------------------------------
# 9.1 print() vs return
# ------------------------------------------------------------

# This function only prints

def add_print(a, b):
    print(a + b)


# This function returns a value

def add_return(a, b):
    return a + b


add_print(5, 3)                    # Prints 8

result = add_return(5, 3)

print(result)                      # 8


# ------------------------------------------------------------
# 9.2 Using a Returned Value
# ------------------------------------------------------------

def calculate_area(width, height):
    area = width * height

    return area


room_area = calculate_area(10, 12)

print(f"Room size: {room_area} sq ft")


# ------------------------------------------------------------
# 9.3 Using Return Values in Expressions
# ------------------------------------------------------------

def double(number):
    return number * 2


# Store in a variable

result = double(5)

print(result)                      # 10


# Use in an expression

total = double(5) + double(3)

print(total)                       # 16


# Pass to another function

print(double(10))                  # 20


# Use in a condition

if double(7) > 10:
    print("Big number!")


# ------------------------------------------------------------
# 9.4 Returning Multiple Values
# ------------------------------------------------------------

def get_min_max(numbers):
    return min(numbers), max(numbers)


# Unpack returned values

minimum, maximum = get_min_max([5, 2, 8, 1, 9])

print(f"Min: {minimum}, Max: {maximum}")


# Or store the returned tuple

result = get_min_max([5, 2, 8, 1, 9])

print(result)                      # (1, 9)


# ------------------------------------------------------------
# 9.5 Functions Without a return Statement
# ------------------------------------------------------------

def greet_user(name):
    print(f"Hello, {name}!")


result = greet_user("Alice")

print(result)                      # None


# ------------------------------------------------------------
# 9.6 Returning Strings
# ------------------------------------------------------------

def get_greeting(name):
    return f"Hello, {name}!"


message = get_greeting("Alice")

print(message.upper())             # HELLO, ALICE!


# ------------------------------------------------------------
# 9.7 Return Ends Function Execution
# ------------------------------------------------------------

def get_status():
    return "Done"

    # This never runs
    # print("This never prints!")


# Better

def get_status():
    print("Checking status...")

    return "Done"


# ------------------------------------------------------------
# 9.8 Common Mistake - Forgetting return
# ------------------------------------------------------------

# Wrong - calculates but doesn't return

def calculate_total_wrong(items):
    total = sum(items)


# Right - return the calculated value

def calculate_total(items):
    total = sum(items)

    return total


# ------------------------------------------------------------
# 9.9 Common Mistake - print Instead of return
# ------------------------------------------------------------

# Wrong

def multiply_wrong(a, b):
    print(a * b)


result = multiply_wrong(3, 4)

# result is None

# This causes an error
# total = result + 10


# Right

def multiply(a, b):
    return a * b


result = multiply(3, 4)

total = result + 10

print(total)                       # 22


# ============================================================
# 10. Local Variables
# ============================================================


# ------------------------------------------------------------
# 10.1 Variables Inside Functions
# ------------------------------------------------------------

def calculate_price():
    price = 100
    tax = price * 0.1

    print(f"Total: {price + tax}")


calculate_price()                   # Total: 110


# ------------------------------------------------------------
# 10.2 Local Variables Cannot Be Accessed Outside
# ------------------------------------------------------------

# This fails because price only exists inside calculate_price()

# print(price)
# NameError: name 'price' is not defined


# ============================================================
# 11. Global Variables
# ============================================================


# ------------------------------------------------------------
# 11.1 Reading a Global Variable
# ------------------------------------------------------------

discount_rate = 0.15


def apply_discount(price):
    discount = price * discount_rate

    return price - discount


result = apply_discount(100)

print(result)                       # 85.0


# ------------------------------------------------------------
# 11.2 Modifying a Global Variable
# ------------------------------------------------------------

counter = 0


def increment():
    global counter

    counter += 1


increment()
increment()

print(counter)                      # 2


# ============================================================
# 12. Avoiding Global State
# ============================================================


# ------------------------------------------------------------
# 12.1 Bad - Using a Global Variable
# ------------------------------------------------------------

total = 0


def add_to_total(amount):
    global total

    total += amount


# ------------------------------------------------------------
# 12.2 Good - Using Parameters and Return
# ------------------------------------------------------------

def add_amounts(current_total, amount):
    return current_total + amount


total = 0

total = add_amounts(total, 10)
total = add_amounts(total, 20)

print(total)                        # 30


# ============================================================
# 13. Mutable Default Arguments
# ============================================================


# ------------------------------------------------------------
# 13.1 Wrong - Mutable Default Argument
# ------------------------------------------------------------

def add_item_wrong(item, items=[]):
    items.append(item)

    return items


# ------------------------------------------------------------
# 13.2 Right - Use None
# ------------------------------------------------------------

def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)

    return items


print(add_item(5))