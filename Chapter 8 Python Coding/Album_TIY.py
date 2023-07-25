def make_album(name, title, tracks= ''):
    ''''Return a dictonary containing an artists' info'''
    
    if tracks:
        person = {'Artist': name.title(), 'Album': title.title(), 'tracks': int(tracks)}
        return person
    else:
        person = {'Artist': name.title(), 'Album': title.title()}
        return person

musican = make_album('khalid', 'american teen')
print(musican)

musican = make_album('kanye west', 'graduation')
print(musican)

musican = make_album('boywithUke', 'serotonin dreams')
print(musican)

musican = make_album('giveon', 'give or take', 15)
print(musican)