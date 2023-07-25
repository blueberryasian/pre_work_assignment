#"input" allows our code to be interactive
#message = input("Tell me something, and I will repeat it back to you: ") 
#print(message)

#name = input("Please enter your name: ")
#print("Hello, " + name + "!")

# += operator means its equal to the line before it plus whatever is being added
#prompt = "If you tell us who you are, we can personalize the messages you see."
#prompt += "\nWhat is your first name? "
#name = input(prompt)
#print("\nHello, " + name + "!")

# Input is automatically stored as a string so you use the int() function when asking about a number 
#height = input("How tall are you, in inches? ")
#height = int(height)
#if height >= 36:
 #print("\nYou're tall enough to ride!")
#else:
 #print("\nYou'll be able to ride when you're a little older.")

# a modulo "%" is the python sign for divide
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
 print("\nThe number " + str(number) + " is even.")
else:
 print("\nThe number " + str(number) + " is odd.")