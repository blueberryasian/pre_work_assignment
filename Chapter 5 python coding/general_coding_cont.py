age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register as soon as you turn 18!")


nage = 20
if nage < 4:
    print("\nYour admission cost is 0$.")
elif nage < 18:
    print("\nYour admission cost is $5.")
else:
    print("\nYour admission cost is $10.")

fage = 12
if fage < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("\nYour admission cost is $" + str(price) + ".")

page = 12
if page < 4:
    rice = 0
elif page < 18:
    rice = 5
elif page < 65:
    rice = 10
else:
    rice = 5
print("\nYour admission cost is $" + str(rice) + ".")

rage = 12
if rage < 4:
    ice = 0
elif rage < 18:
    ice = 5
elif rage < 65:
    ice = 10
elif rage >= 65:
    ice = 5
print("\n Your admission cost is $" + str(ice) + ".")
