cities = {
    'paris': {
        'country': 'france',
        'population': 2000000,
        'fact': 'the eiffel tower is there'
    },
    
    'honolulu':{
        'country':'USA',
        'population': 345000,
        'fact': 'honolulu has lots of volcanos'
    },

    'rome': {
        'country': 'italy',
        'population': 4400000 ,
        'fact': 'rome was discovered bce'
    },
    }

for city, info in cities.items():
    print("\n" + city.title() + ", ")
    c = info['country']
    p = info['population']
    fact = info['fact']
    print(c.title() + " has a population of " + str(p))
    print(" and a fun fact is " + fact + "!") 