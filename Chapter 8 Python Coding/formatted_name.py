## A return function processes the data then returns a value which called a return value as shown below:
## You will also need a variable where the return value can be stored in this case it is "musician"

#def get_formatted_name(first_name, last_name):
 #   """Return a full name, neatly formatted."""
  #  full_name = first_name + ' ' + last_name
   # return full_name.title()

#musician = get_formatted_name('jimi', 'hendrix')
#print(musician)

## You can also make an argument optional so people using the function only if they WANT to by setting the default value to an empty string

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)