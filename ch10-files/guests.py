from pathlib import Path

current_number = 1
names_list = ''

while current_number <= 5:
  name = input("What is your first and last name? ")
  greeting = f"Hello {name.title()}!"
  print(greeting)
  names_list += f"{name}\n"
  current_number += 1

path = Path('ch10-files/guest_book.txt')
path.write_text(names_list.rstrip())