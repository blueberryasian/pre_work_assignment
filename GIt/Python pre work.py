def hello_name(user_name):
    '''
    Display the persons username
    '''
    print('Hello! '+
          user_name.title())
    

def odd_first():
    '''
    Print odd numbers
    '''
    for i in range(1, 100, 2):
        print(i)
    
  


def max_numb_in_list(a_list):
    '''
    Return max number in a list
    '''
    max_num = max(a_list)
    return max_num


def is_leap_year(a_year):
    '''
    Checking if it a leap year
    '''
    if a_year % 400 == 0:
        return True
    elif a_year % 4 == 0 and a_year % 100 != 0:
        return True
    else:
        return False

            
            

def is_consecutive(a_list):
     '''
     Checking a list to see if the numbers are consectuive
     '''
     if a_list:
          return sorted(a_list) == list(range(min(a_list), max(a_list)+1))
     else:
          return False
     
          



    


        


