print("This program will find the sum of your numbers!")

user_number1 = input("Enter a number: ")
user_number2 = input("Enter a second number: ")

try:
  addition_sum = int(user_number1) + int(user_number2)
except ValueError:
  print("You can only enter numeric values!")
else:
  print(f"The sum of your numbers is {addition_sum}.")
