# # Subscripting
# print("Hello"[0])

# # String
# print("123" + "456")

# # Integer = Whole number
# print(123 + 456)

# # Large Integers
# print(123_456_789)

# # Float = Floating Point Number
# print(3.14159)

# # Boolean = True or False
# print(True)
# print(False)

# print(type("Hello"))
# print(type(123))
# print(type(3.14))
# print(type(True))

# print(6 + 4 / 2 - (1 * 2))

# a = int("5") / int(2.7)
# print(type(a))

print("Welcome to the tipo calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip = total_bill * (tip_percentage / 100)
total_bill_with_tip = total_bill + tip
amount_per_person = total_bill_with_tip / people
print(f"Each person should pay: ${amount_per_person:.2f}")