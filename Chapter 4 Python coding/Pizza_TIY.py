pizzas = ["pepperoni" , "cheese" , "hawaiian"]
for pizza in pizzas:
    print("I love " + pizza.title() + " pizza, it's soooo tasty" + "!\n")
print("Pepperoni pizza is so unique, there's nothing like!\n" + "Cheese pizza is so cultural, Italians went crazy!\n" + "Hawaiian pizza should be studied in schools\n")
print("I really love pizza")
my_pizzas = pizzas
friends_pizzas = my_pizzas[:]
print(my_pizzas)
print(friends_pizzas)
my_pizzas.append("threemeat")
friends_pizzas.append("veggie")
print("My favorite pizzas are:")
print(my_pizzas)
print("My favorite pizzas are:")
for me in my_pizzas:
    print(me)
print("\nMy friend's favorite pizzas are:")
for friend in friends_pizzas:
    print(friend)