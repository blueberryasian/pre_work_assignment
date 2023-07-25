## This is a function with multiple parameters. parameters = variable  argument = value

#def describe_pet(animal_type, pet_name):
 #"""Display information about a pet."""
 #print("\nI have a " + animal_type + ".")
 #print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#describe_pet('hamster', 'harry')

## You can do more than one function call with the same layout! As shown below!:

#describe_pet('dog' , 'willie')

## Keyword arguments arrange it so you don't have to worry about the order of the arguments in question:

#def describe_pet(animal_type, pet_name):
 #"""Display information about a pet."""
 #print("\nI have a " + animal_type + ".")
 #print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#describe_pet(animal_type='hamster', pet_name='harry')
#describe_pet(pet_name='harry', animal_type='hamster')

## When you define a default value for a parameter you can exclude the corresponding argument as shown below!:
## dog is just the default value you can still use a different value for the parameter if you choose to do so

def describe_pet(pet_name, animal_type='dog'):
 """Display information about a pet."""
 print("\nI have a " + animal_type + ".")
 print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')
describe_pet('rex', 'dinosaur')