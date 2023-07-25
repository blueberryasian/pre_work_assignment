## You can use functions with all these structures such as for loops and while loops

def get_formatted_name(first_name, last_name):
   """Return a full name, neatly formatted."""
   full_name = first_name + ' ' + last_name
   return full_name.title()

#while True:
 #  print("\nPlease tell me your name:")
  # f_name = input("First name: ")
   #l_name = input("Last name: ")
   
   #formatted_name = get_formatted_name(f_name, l_name)
   #print("\nHello, " + formatted_name + "!") 

## The formula above is an infinite loop in order to combat we need to enter a break statement

def get_formatted_name(first_name, last_name):
   '''Return a full name neatly formatted'''
   full_name = first_name + ' ' + last_name
   return full_name.title()

while True:
   print("\nPlease tell me your name:")
   print("(enter 'q' at anytime to quit)")

   f_name = input('First name: ')
   if f_name == 'q':
      break
   
   l_name = input('Last name: ')
   if l_name == 'q':
      break
   
   formatted_name = get_formatted_name(f_name, l_name)
   print("\nHello, " + formatted_name + '!')