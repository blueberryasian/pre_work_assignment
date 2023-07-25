user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }
for name, language in favorite_languages.items():
     print(name.title() + "'s favorite language is " +
           language.title() + ".")
     for name in favorite_languages.keys():
          print(name.title())

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
 print(name.title())

 if name in friends:
     print(" Hi " + name.title() +
           ", I see your favorite language is " +
             favorite_languages[name].title() + "!")
     
     favorite_languages = {
         'jen': 'python',
         'sarah': 'c',
         'edward': 'ruby',
         'phil': 'python',
         }
 if 'erin' not in favorite_languages.keys():
     print("Erin, please take our poll!")

#How to loop through dictonary keys in order

     favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for name in sorted(favorite_languages.keys()):
 print(name.title() + ", thank you for taking the poll.")

 #Use .keys() to pull keys and .value() to pull the values. For example:
 favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
print("The following languages have been mentioned:")
for language in favorite_languages.values():
 print(language.title())

 #Using "set" in a for loop makes sure there is no repetion in the list. For example:
 favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
        print(language.title())