sandwich_orders = ['tuna' , 'meatball' , 'ham' , 'turkey']
finished_sandwiches = []

while sandwich_orders:
    orders = sandwich_orders.pop()
    print('Making the ' + orders.title() + ' sandwich!')
    finished_sandwiches.append(orders)

print("\nThe following sanwiches are ready for pickup:")
for finished in finished_sandwiches:
    print(finished.title())
