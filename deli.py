ordered_sandwiches = [
    'classic clubhouse',
    'veggie delight',
    'smoky chicken',
    'turkey avocado',
    'spicy hummus crunch'
]

finished_sandwiches = []

while ordered_sandwiches:
    ordered_sandwich = ordered_sandwiches.pop()

    print(f"I've made your {ordered_sandwich} Sandwich.")
    finished_sandwiches.append(ordered_sandwich)

print("\nThe following ordered sandwiches have been finished:")

for finished_sandwich in finished_sandwiches:
    print(fincished_sandwich.title())
