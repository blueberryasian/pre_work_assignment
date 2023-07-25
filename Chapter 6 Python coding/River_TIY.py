rivers = {
    'nile': 'egypt',
    'rio grande': 'mexico',
    'amazon': 'peru'
}

for river, place in rivers.items():
    print("The " + river.title() + ",")
    print(" runs through " + place.title() + "!\n")
for river in rivers.keys():
    print(river.title())
for place in rivers.values():
    print(place.title())