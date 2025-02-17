major_rivers = {
    'mississippi': 'united states',
    'amazon': 'brazil',
    'yangtze': 'china'
    }

for river, country in major_rivers.items():
    print(f'The {river.title()} river runs through {country.title()}.')