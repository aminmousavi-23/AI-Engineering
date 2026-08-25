# ============================================================
# Operators & String Manipulation
# ============================================================


# ------------------------------------------------------------
# 1. Arithmetic Operators
# ------------------------------------------------------------

average = (10 + 20 + 30) / 3
print(average)


# Regular division
result = 10 / 2
print(result)                   # 5.0


# Integer / Floor division
result = 10 // 2
print(result)                   # 5


# ------------------------------------------------------------
# 2. String Formatting - f-strings
# ------------------------------------------------------------

name = "Amin"

string = f"Hi my name is {name}."

print(string)


# ------------------------------------------------------------
# 3. String Case Methods
# ------------------------------------------------------------

print(string.lower())
print(string.upper())
print(string.title())


# ------------------------------------------------------------
# 4. Removing Whitespace
# ------------------------------------------------------------

messy = "  hello world  "

print(messy.strip())            # "hello world"


# ------------------------------------------------------------
# 5. Removing Characters
# ------------------------------------------------------------

price = "$19.99"

print(price.strip("$"))         # "19.99"


# ------------------------------------------------------------
# 6. Checking String Content
# ------------------------------------------------------------

message = "I love Python programming with Python"

print("Python" in message)              # True
print(message.startswith("I"))         # True
print(message.endswith("Python"))      # True


# ------------------------------------------------------------
# 7. Finding Text
# ------------------------------------------------------------

print(message.find("Python"))           # 7
print(message.count("Python"))          # 2


# ------------------------------------------------------------
# 8. Replacing Text
# ------------------------------------------------------------

new_message = message.replace("Python", "JavaScript")

print(new_message)
# "I love JavaScript programming with JavaScript"