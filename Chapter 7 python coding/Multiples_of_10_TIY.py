message = input("Please type in a number and we'll let you know if its a multiple of 10.: ")
message = int(message)

if message % 10 == 0:
    print("Yes " + str(message) + " is a multiple of 10!")
else:
    print("No " + str(message) + " is not a multiple of 10.")
    print(message)