#(The += operator is shorthand for current_number = current_number + 1.) 

#current_number = 1
#while current_number <= 5:
 #print(current_number)
 #current_number += 1

# We put an empty string in "message" so Pythhon has something to compare to and will continue the while loop.

#prompt = "\nTell me something, and I will repeat it back to you:"
#prompt += "\nEnter 'quit' to end the program. "
#message = ""
#while message != 'quit':
 #message = input(prompt)
 #print(message)

# We use an "if test" in order to stop making thhe program repeat the word quit

#prompt = "\nTell me something, and I will repeat it back to you:"
#prompt += "\nEnter 'quit' to end the program. "

#message = ""

#while message != 'quit':
 #message = input(prompt)

 #if message != 'quit':
  # print(message)

# We can use the 'break' function to exit a while loop without any remaining code

#prompt = "\nPlease enter the name of a city you have visited:"
#prompt += "\n(Enter 'quit' when you are finished.) "

#while True:
#  city = input(prompt)
  
 # if city == 'quit':
   #break
  #else:
   #print("I'd love to go to " + city.title() + "!")

# We can use a continue statement to return to the beginning of a loop based on a conditional test rather than stopping it all together

#current_number = 0
#while current_number < 10:
    
 #   current_number += 1
  #  if current_number % 2 == 0:
   #    continue
    
    #print(current_number)

# Example of an infinite loop
# If you forget the += operator the loop will run forever

x = 1
while x <= 5:
    print(x)

