# ============================================================
# Object-Oriented Programming (OOP)
# ============================================================


# ============================================================
# 1. Creating Classes and Objects
# ============================================================


# ------------------------------------------------------------
# 1.1 Creating a Class
# ------------------------------------------------------------


class APIConfig:
    pass


# ------------------------------------------------------------
# 1.2 Creating Objects
# ------------------------------------------------------------

dev_config = APIConfig()
prod_config = APIConfig()


# ============================================================
# 2. __init__ and Instance Attributes
# ============================================================


# ------------------------------------------------------------
# 2.1 The __init__ Method
# ------------------------------------------------------------


class APIConfig:
    def __init__(self, api_key, model="gpt-3.5-turbo", max_tokens=100):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com/v1"


# ------------------------------------------------------------
# 2.2 Creating Objects with Arguments
# ------------------------------------------------------------

# Positional argument + named argument

dev_config = APIConfig("sk-dev-key", max_tokens=50)


# All named arguments

prod_config = APIConfig(api_key="sk-prod-key", model="gpt-4", max_tokens=1000)


# ------------------------------------------------------------
# 2.3 Accessing Instance Attributes
# ------------------------------------------------------------

print(dev_config.model)  # gpt-3.5-turbo
print(prod_config.model)  # gpt-4
print(prod_config.max_tokens)  # 1000


# ------------------------------------------------------------
# 2.4 Instance Attributes Are Unique to Each Object
# ------------------------------------------------------------


class APIClient:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url
        self.request_count = 0


client1 = APIClient(api_key="key1", base_url="https://api1.com")

client2 = APIClient(api_key="key2", base_url="https://api2.com")


print(client1.api_key)  # key1
print(client2.api_key)  # key2


# ============================================================
# 3. Methods
# ============================================================


# ------------------------------------------------------------
# 3.1 Creating Methods
# ------------------------------------------------------------


class DataValidator:
    def __init__(self):
        self.errors = []

    def validate_email(self, email):
        if "@" not in email:
            self.errors.append(f"Invalid email: {email}")
            return False

        return True

    def validate_age(self, age):
        if age < 0 or age > 150:
            self.errors.append(f"Invalid age: {age}")
            return False

        return True

    def get_errors(self):
        return self.errors


# ------------------------------------------------------------
# 3.2 Calling Methods
# ------------------------------------------------------------

validator = DataValidator()


# Notice:
# We don't pass self manually.

validator.validate_email(email="bad-email")

validator.validate_age(age=200)


# Positional arguments also work

validator.validate_email("another-bad-email")

validator.validate_age(150)


print(validator.get_errors())


# ============================================================
# 4. Class Attributes
# ============================================================


# ------------------------------------------------------------
# 4.1 Class Attributes
# ------------------------------------------------------------


class APIClient:
    version = "1.0"
    max_retries = 3

    def __init__(self, api_key):
        self.api_key = api_key


client1 = APIClient("key1")
client2 = APIClient("key2")


# Class attributes are available through objects

print(client1.version)  # 1.0
print(client2.version)  # 1.0

print(client1.max_retries)  # 3
print(client2.max_retries)  # 3


# They can also be accessed through the class

print(APIClient.version)  # 1.0
print(APIClient.max_retries)  # 3


# ------------------------------------------------------------
# 4.2 Instance vs Class Attributes
# ------------------------------------------------------------

# Instance attribute - unique to each object

print(client1.api_key)  # key1
print(client2.api_key)  # key2


# Class attribute - shared default for the class

print(client1.version)  # 1.0
print(client2.version)  # 1.0


# ============================================================
# 5. Inheritance
# ============================================================


# ------------------------------------------------------------
# 5.1 Parent Class
# ------------------------------------------------------------


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"

    def sleep(self):
        return f"{self.name} is sleeping"


# ------------------------------------------------------------
# 5.2 Child Class
# ------------------------------------------------------------


class Dog(Animal):
    def bark(self):
        return f"{self.name} says woof!"


# ------------------------------------------------------------
# 5.3 Using an Inherited Class
# ------------------------------------------------------------

my_dog = Dog("Buddy")

my_dog2 = Dog(name="Max")


# Dog inherits methods from Animal

print(my_dog.eat())
print(my_dog.sleep())


# Dog also has its own method

print(my_dog.bark())


# ============================================================
# 6. super()
# ============================================================


# ------------------------------------------------------------
# 6.1 Calling the Parent __init__
# ------------------------------------------------------------


class Animal:
    def __init__(self, name):
        self.name = name
        self.is_pet = True


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)

        self.breed = breed

    def describe(self):
        return f"{self.name} is a {self.breed}"


# ------------------------------------------------------------
# 6.2 Creating Child Objects
# ------------------------------------------------------------

golden = Dog("Buddy", "Golden Retriever")

poodle = Dog(name="Max", breed="Poodle")


print(golden.describe())

# Attribute inherited from Animal

print(golden.is_pet)


# ============================================================
# 7. Method Overriding
# ============================================================


# ------------------------------------------------------------
# 7.1 Overriding a Parent Method
# ------------------------------------------------------------


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return f"{self.name} makes a sound"


class Dog(Animal):
    def make_sound(self):
        return f"{self.name} barks: Woof!"


class Cat(Animal):
    def make_sound(self):
        return f"{self.name} meows: Meow!"


# ------------------------------------------------------------
# 7.2 Different Implementations
# ------------------------------------------------------------

generic = Animal(name="Something")

dog = Dog(name="Buddy")

cat = Cat(name="Whiskers")


print(generic.make_sound())
print(dog.make_sound())
print(cat.make_sound())


# ============================================================
# 8. Real-World Example
# ============================================================


# ------------------------------------------------------------
# 8.1 Base Model
# ------------------------------------------------------------


class BaseModel:
    def __init__(self, model_name):
        self.model_name = model_name
        self.is_loaded = False

    def load(self):
        print(f"Loading {self.model_name}...")

        self.is_loaded = True


# ------------------------------------------------------------
# 8.2 Text Model
# ------------------------------------------------------------


class TextModel(BaseModel):
    def __init__(self, model_name, max_length=1000):
        super().__init__(model_name)

        self.max_length = max_length

    def process_text(self, text):

        if not self.is_loaded:
            self.load()

        if len(text) > self.max_length:
            text = text[: self.max_length]

        return f"Processed: {text}"


# ------------------------------------------------------------
# 8.3 Using the Model
# ------------------------------------------------------------

model = TextModel(model_name="gpt-3.5-turbo", max_length=100)


result = model.process_text(text="Hello world")

print(result)


# ============================================================
# End of OOP
# ============================================================
