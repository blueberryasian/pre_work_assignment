# We use a variable called a flag that acts as a signal to the program to allow it to continue, if at any point a condition is broken the flag will tell the program to stop

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
   message = input(prompt)
   
   if message == 'quit':
     active = False
else:
   print(message)