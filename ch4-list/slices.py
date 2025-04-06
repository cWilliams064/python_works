guests = ['elizabeth short', 'ora murray', 'jonbenet ramsey']

invitation = f"{guests[0].title()}, you are invited to a dinner reservation hosted by Courtney Williams."
print(invitation)

invitation = f"{guests[1].title()}, you are invited to a dinner reservation hosted by Courtney Williams."
print(invitation)

invitation = f"{guests[2].title()}, you are invited to a dinner reservation hosted by Courtney Williams."
print(invitation)

print("I found a biger dinner table for more guests.")

guests.insert(0, 'marilyn monroe')
guests.insert(1, 'joseph zarelli')
guests.append('maria ridulph')

guests.sort()

invitation = f"{guests[0].title()}, you are invited to a dinner reservation hosted by Courtney Williams."
print(invitation)

invitation = f"{guests[1].title()}, you are invited to a dinner reservation hosted by Courtney Williams."
print(invitation)

invitation = f"{guests[2].title()}, you are invited to a dinner reservation hosted by Courtney Williams."
print(invitation)

invitation = f"{guests[3].title()}, you are invited to a dinner reservation hosted by Courtney Williams."
print(invitation)

invitation = f"{guests[4].title()}, you are invited to a dinner reservation hosted by Courtney Williams."
print(invitation)

invitation = f"{guests[5].title()}, you are invited to a dinner reservation hosted by Courtney Williams."
print(invitation)

print('The first three items in the list are:')
print(guests[:3])

print('Three items from the middle of the list are:')
print(guests[1:4])

print('The last three items in the list are:')
print(guests[-3:])