def describe_city(city, country = 'The usa'):
    '''Describing what cities are in which countries'''
    print('\n' + city.title() + ' is in ' + country.title() + '!')

describe_city('san diego')
describe_city('new york city')
describe_city('paris', country= 'france')