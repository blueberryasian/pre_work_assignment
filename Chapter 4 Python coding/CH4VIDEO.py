#grocery_list = ['apple' , 'banana', 'orange', 'spinach', 'kale' , 'curry', 'potatoes', 'quiche', 'quinoa']

#my_enumeration_station = list(enumerate(grocery_list))
#print(my_enumeration_station)

#print(type(my_enumeration_station[4]))

#my_tup = ('cats' , 5)

nums_one = [1,2,3]
nums_two = [3,4,5]

prompt = "Find all the unique numbers between two sets"

new_list = set(nums_one + nums_two)
for i in new_list:
    print(i)