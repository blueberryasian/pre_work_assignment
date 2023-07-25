## Sometimes you won't know how many arguments a function needs so we use an asterisk to create an empty tuple

#def make_pizza(*toppings):
 #"""Print the list of toppings that have been requested."""
 #print('\nMaking a pizza with the following toppings:')
 #for topping in toppings:
 # print('- ' + topping)

#make_pizza('pepperoni')
#make_pizza('mushrooms', 'green peppers', 'extra cheese')  

## If you want a function to accept multiple arguments the parameter must be placed at the end for example:

#def make_pizza(size, *toppings):
 #"""Summarize the pizza we are about to make."""
 #print("\nMaking a " + str(size) +
 #"-inch pizza with the following toppings:")
 #for topping in toppings:
  # print("- " + topping)

#make_pizza(16, 'pepperoni')
#make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

## You can also write functions that accept many key-value pairs using double asterisk for example:

def build_profile(first, last, **user_info):
 """Build a dictionary containing everything we know about a user."""
 profile = {}
 profile['first_name'] = first
 profile['last_name'] = last
 for key, value in user_info.items():
      profile[key] = value
      return profile
 
user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

