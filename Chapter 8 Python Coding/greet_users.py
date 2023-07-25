## Sometimes it is useful to pass a list to a function for example:

def greet_users(names):
 """Print a simple greeting to each user in the list."""
 for name in names:
   msg = "Hello, " + name.title() + "!"
   print(msg)

   
usernames = ['jelly', 'colin', 'tylerthecreator']
greet_users(usernames)