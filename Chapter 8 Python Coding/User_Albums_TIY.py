def make_album(name, title):
    ''''Return a dictonary containing an artists' info'''

    artist = {'Artist: ': name.title() ,'Album: ': title.title()}
    return artist
   
while True:
        print('\nWho is your favorite artist?: ')
        print('What is your favorite album from them?: ')
        print('Enter "q" at anytime to quit')
        
       
        singer = input('Artist: ' )
        if singer == 'q':
            break

        album = input('Album: ' )
        if album == 'q':
             break
        
        music = make_album(singer, album)
        print(music)