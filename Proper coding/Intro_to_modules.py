## You can store information in whats called a "module" where you can then import it into any program

## To call any function from an imported module enter the name of the module seperated by a dot and then the function: module_name.function_name()

## You can a specific function from a module using: from module_name import function_name

## You can import as many as you want as long as you seperate them with a comma: from module_name import function_0, function_1, function_2

## You can also give a function an alias or nickname: from module_name import funcrion_name as fn

## You can do thhe samne thing for modules: import module_name as mn

## You can tell Python to import every function in a module by using an asterisk* : from pizza import *

## When writing a function make sure to have a clear description so other people can use

## If you specify a default value for a parameter no spaces should be used on either side: def function_nsmr(parameter_0, parameter_1='default value')

## Same for keyword arguments: function_name(value_0, parameter_1='value')

## Example of code following PEP8 guidelines, you press tab twice to seperate the list of arguments from the body

def function_name(
        parameter_0, parameter_1, parameter_2,
        parameter_3, parameter_4, parameter_5):
  function body...