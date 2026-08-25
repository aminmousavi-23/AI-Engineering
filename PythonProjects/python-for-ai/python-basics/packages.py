# ============================================================
# Modules, Imports and Packages
# ============================================================


# ============================================================
# 1. Importing Modules
# ============================================================


# ------------------------------------------------------------
# 1.1 Import the Whole Module
# ------------------------------------------------------------

import math


result = math.sqrt(16)

print(result)                    # 4.0


# ------------------------------------------------------------
# 1.2 Import Specific Items
# ------------------------------------------------------------

from math import sqrt, pi


result = sqrt(16)

print(result)                    # 4.0


radius = 5

circle_area = pi * radius ** 2

print(circle_area)


# ------------------------------------------------------------
# 1.3 Import with an Alias
# ------------------------------------------------------------

import datetime as dt


today = dt.date.today()

print(today)


# ============================================================
# 2. Standard Library Modules
# ============================================================


# ------------------------------------------------------------
# 2.1 random
# ------------------------------------------------------------

import random


number = random.randint(1, 10)

choice = random.choice([
    "apple",
    "banana",
    "orange"
])

print(number)
print(choice)


# ------------------------------------------------------------
# 2.2 datetime
# ------------------------------------------------------------

import datetime


today = datetime.date.today()

print(today)


# ------------------------------------------------------------
# 2.3 os
# ------------------------------------------------------------

import os


current_dir = os.getcwd()

print(current_dir)


# ------------------------------------------------------------
# 2.4 json
# ------------------------------------------------------------

import json


data = {
    "name": "Alice",
    "age": 30
}

json_string = json.dumps(data)

print(json_string)


# ============================================================
# 3. Importing Third-Party Packages
# ============================================================


# ------------------------------------------------------------
# 3.1 requests
# ------------------------------------------------------------

import requests


response = requests.get(
    "https://api.example.com/data"
)

data = response.json()

print(data)


# ------------------------------------------------------------
# 3.2 pandas
# ------------------------------------------------------------

import pandas as pd


data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["NYC", "LA", "Chicago"]
}

df = pd.DataFrame(data)

print(df)


# ============================================================
# 4. Import Everything
# ============================================================


# Avoid this style

# from math import *


# Prefer explicit imports

from math import sqrt, pi


# ============================================================
# 5. Naming Conflicts
# ============================================================


# Wrong - overwrites the module name

import datetime

# datetime = "2024-01-01"


# Right - use a different variable name

import datetime

date_string = "2024-01-01"

print(date_string)


# ============================================================
# 6. Installing Packages with pip
# ============================================================


# ------------------------------------------------------------
# 6.1 Install a Package
# ------------------------------------------------------------

# pip install requests


# ------------------------------------------------------------
# 6.2 Install a Specific Version
# ------------------------------------------------------------

# pip install requests==2.28.0


# ------------------------------------------------------------
# 6.3 Install Multiple Packages
# ------------------------------------------------------------

# pip install pandas numpy matplotlib


# ============================================================
# 7. requirements.txt
# ============================================================


# A requirements.txt file lists project dependencies.


# Generate requirements.txt

# pip freeze > requirements.txt


# Install dependencies from requirements.txt

# pip install -r requirements.txt


# Example requirements.txt:
#
# certifi==2024.2.2
# charset-normalizer==3.3.2
# idna==3.6
# requests==2.31.0
# urllib3==2.2.0


# ============================================================
# 8. ModuleNotFoundError
# ============================================================


# Wrong - package isn't installed in the current environment

# import pandas
#
# ModuleNotFoundError


# Right - install the package first

# pip install pandas

import pandas


# ============================================================
# End of Modules, Imports and Packages
# ============================================================