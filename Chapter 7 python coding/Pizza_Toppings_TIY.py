prompt = input("\nWhat would you like on your pizza?: ")
prompt += ("\nEnter quit when you are done: ")

while True:
    pizza = input(prompt)

    if pizza == 'quit':
        break
    else:
        print("Great choice adding " + pizza.title() + " to your pizza!" )
        print(pizza)