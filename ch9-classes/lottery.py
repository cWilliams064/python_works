from random import choice

def winning_tickets():
  """Combines random number with letter for winning tickets."""
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  letters = ['a', 'b', 'c', 'd', 'e']
  combination = str((choice(numbers))) + choice(letters).capitalize()
  print(f"If you have ticket {combination} your a winner!")

winning_tickets()
winning_tickets()
winning_tickets()
