dimensions = (200, 50)
print(dimensions[0])
#print(dimensions[1])=250 Can't change the items in a Tuple, you can only access them
for dimension in dimensions:
    print(dimension) 
    dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
 print(dimension)
dimensions = (400, 100) 
print("\nModified dimensions:")
for dimension in dimensions:
 print(dimension)