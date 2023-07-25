favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

poll = ['jen' , 'phil' , 'jelly' , 'colin']
for name in poll:
    if name in favorite_languages:
        print("Thanks for responding, " + name.title())
    else:
        print("Hey " + name.title() + ", come take our poll!")