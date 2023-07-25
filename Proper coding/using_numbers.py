for value in range(1,6):
 print(value)
 numbers = list(range(1,6))
print(numbers)
#How to sort through even numbers 2 is 1 and 11 is 10 and the second 2 is what its counting by
even_numbers = list(range(2,11,2))
print(even_numbers)
#InPython, two asterisks (**) represent exponents. Here’s how you might put the first 10 square numbers into a list:
squares = []
for value in range(1,11):
   square = value**2
   squares.append(square)
print(squares)
#To write this code more concisely, omit the temporary variable square and append each new value directly to the list:
squares = []
for value in range(1,11):
  squares.append(value**2)
print(squares)
#A few Python functions are specific to lists of numbers. For example, you can easily find the minimum, maximum, and sum of a list of numbers:
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))  
print(sum(digits))
#To use this syntax, begin with a descriptive name for the list, such as
#squares. Next, open a set of square brackets and define the expression for
#the values you want to store in the new list. In this example the expression is value**2, which raises the value to the second power. Then, write
#a for loop to generate the numbers you want to feed into the expression,
#and close the square brackets. The for loop in this example is for value
#in range(1,11), which feeds the values 1 through 10 into the expression
#value**2. Notice that no colon is used at the end of the for statement.
#The result is the same list of square numbers you saw earlier:
squares = [value**2 for value in range(1,11)]
print(squares)
