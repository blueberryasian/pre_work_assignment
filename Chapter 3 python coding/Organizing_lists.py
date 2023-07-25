#Organizing a list in alphabetical order(permanent)
animals = ["dog" , "cat" , "bird" , "fox" , "monkey"]
animals.sort()
print(animals)
#Organizing a list in reverse alphabetical order(permanent)
animals.sort(reverse=True)
print(animals)
#How to temporaily present it sorted but its remains the same
print("Here is the original list:")
print(animals)
print("\nHere is the sorted list:")
print(sorted(animals))
print("\nHere is the original list again:")
print(animals)
#How to print a list in reverse order
print("\nReverse order below:")
animals = ["dog" , "cat" , "bird" , "fox" , "monkey"]
print(animals)
animals.reverse()
print(animals)
#How to find the length of a list
print(len(animals))
