def make_shirt(size='large', text='i love python'):
    '''Creating a shirt'''
    print('\nI would like my shirt in a ' + size.title() + '.')
    print('And I want it to say, ' + text.title() + '!')

make_shirt()
make_shirt(size= 'medium')
make_shirt(size='small', text= 'i\'m scared of the gym' )