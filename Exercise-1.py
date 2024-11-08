# Question 1: Variable Assignment and String Manipulation
print("Hey user, what is your name and age?")
name = input("Enter name: ")
username = name
age = input("Enter age: ")
user_age = age

# Question 2: Integer Operations
print("Hey," + username, "type in the length and width of a rectangle")
length = int(input("Length: "))

user_length = length
width = int(input("Width: "))
user_width = width

area = user_length * user_width
print("Area = ", + area)

# Question 3: Working with Floats
print("Hey," + username, "type in temperature in Celsius")
Celsius = float(input("Celsius: "))
user_temperature = Celsius

Fahrenheit = (Celsius * 9/5) + 32
print("Fahr0enheit = ", + Fahrenheit)