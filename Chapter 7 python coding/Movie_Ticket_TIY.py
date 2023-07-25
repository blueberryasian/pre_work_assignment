message = input("How are old are you?: ")
ticket = int(message)

if ticket < 3:
    print("Your ticket is free!")
elif ticket <= 12:
    print("You're ticket will be 10$!")
else:
    print("Your ticket will be 15$!")