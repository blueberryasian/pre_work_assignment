def make_car(make, model, **optional):
    '''Give us information about cars'''
    car = {}
    car['brand'] = make
    car['model'] = model
    for key, value in optional.items():
        car[key] = value
        return car
    
new_car = make_car('hyundai', 'accent', color='red',year='2016')
print(new_car)

