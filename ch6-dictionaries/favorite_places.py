favorite_places = {
    'katelyn': ['forks, washington', 'los angeles, california'],
    'jessica': ['myrtle beach, south carolina'],
    'courtney': ['indianapolis, indiana', 'soul, south korea']
    }

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")