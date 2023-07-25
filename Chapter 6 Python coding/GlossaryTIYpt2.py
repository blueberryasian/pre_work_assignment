glossary = {'strip': 'to get rid of white space',
            'title function': 'to capitialize the first letter',
            'tuple': 'a list that can not be changed',
            'if chain': 'testing a value',
            'conditional test': 'checking if a test passes conditions',
            'set': 'used in a for loop in order to not have repeats',
            'for loop': 'checks every value in a list',
            'dictonary': 'variable that holds keys and values',
            'float': 'number that includes a decimal',
            'interger': 'a number used in coding'
            }
for terms, defintions in glossary.items():
    print(terms.title() + ":")
    print(defintions.title() + "\n")