#Items in a list start at 0 not 1
positions = ["doggystyle" , "cowgirl" , "missionary" , "sixtynine"]
print(positions[0].title())
print(positions[1].upper())
print(positions[2].lower())
print(positions[-1].title())
message = "My favoite position is " + positions[0].title() + "."
print(message)
message = "I would love to do " + positions[2].title() + " with my girlfriend Jelly right now!"
print(message)
message = "people who's favorite postion is " + positions[-1] + " are just plain crazy!!!"
print(message)
#Code below this message is how you change an item in a list
positions[3] = "anal" 
print(positions[3])
#Code below is how you add new elements to a list
positions.append("flatiron")
print(positions)
fastfood = []
fastfood.append("burger king")
fastfood.append("mcdonalds")
fastfood.append("innout")
print(fastfood)
#Code below is how to add to lists in the exact spot you want it
fastfood.insert(0, "tacobell")
print(fastfood)
#Code below is how you remove any item from a list
del fastfood[2]
print(fastfood)
#Popping items from a list is removing it from the list but still being able to use the value
popped_fastfood = fastfood.pop()
print(fastfood)
print("the last thing i ate this year was a burger from " + popped_fastfood.title() + ".")
today = fastfood.pop(0)
print("The first thing i ate today was " + today.title())
fastfood.append("mcdonalds")
fastfood.append("innout")
fastfood.insert(0, "tacobell")
print(fastfood)
#Code below is how you remove item by value which is by its name
fastfood.remove("mcdonalds")
print(fastfood)
nasty = "burger king"
fastfood.remove(nasty)
print(fastfood)
print("\nAll of " + nasty.title() + " taste like shit to me.")