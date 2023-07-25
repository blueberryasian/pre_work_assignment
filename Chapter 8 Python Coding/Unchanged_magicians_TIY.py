def show_magicians(magicians):
    '''Display magician name'''
    for magician in magicians:
        print(magician.title())

magicians = ['colin', 'jelly', 'peanut']
great_magicians = []

def make_great(magicians):
    '''Add the great'''
    while magicians:
        changing = magicians.pop()
        print(changing.title() + ' the Great')
        great_magicians.append(changing)

make_great(magicians)

show_magicians(magicians)
print('\n')
show_magicians(great_magicians)









