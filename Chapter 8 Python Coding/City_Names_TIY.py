def city_country(city, country):
    '''Display a city and It's country in neat format'''
    cityname = city + ', ' + country
    return cityname.title()

deez = city_country('paris', 'france')
print(deez)

deez = city_country('new york', 'united states')
print(deez)

deez = city_country('phnom penh', 'cambodia')
print(deez)