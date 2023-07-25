def build_sandwich(bread, *toppings):
    '''Building a sandwich'''
    print('\nMaking on a sandwich on ' + bread.title())
    print('The toppings on the sandwich are: ' + str(toppings))
    for topping in toppings:
        print(topping)

build_sandwich('rye', 'pepperoni', 'salami', 'balsalmic vinegar')
build_sandwich('italian', 'meatball')
build_sandwich('cheesy', 'barbecue sauce', 'onions', 'spinach')
