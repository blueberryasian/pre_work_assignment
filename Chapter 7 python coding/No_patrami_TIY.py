sandwich_orders = ['tuna' , 'pastrami', 'meatball', 'pastrami' , 'ham' , 'pastrami' , 'turkey']
finished_sandwiches = []
print(sandwich_orders)

print("Sorry everyone we have run out of patrami!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    

while sandwich_orders:
        orders = sandwich_orders.pop()
        print('\tMaking the ' + orders.title() + ' sandwich!')
        finished_sandwiches.append(orders)

print("\nThe following sanwiches are ready for pickup:")
for finished in finished_sandwiches:
    print(finished.title())
