## If statements:

#if case1:
 #   perform action1
#elif case2:
 #   perform action2
#else:
  #  perform action 3

#x = int(input("Please enter an integer: "))

#if x < 0:
 #   x = 0
  #  print('Negative changed to zero')
#elif x == 0:
#     print('Zero')
#elif x == 1:
 #        print('Single')
#else:
 #        print('More')

## Function syntax:

def is_prime(num):
            '''
            Naive method of checking for primes.
            '''
            for n in range(2,num):
                if num % n == 0:
                    print ('not prime')
                    break
            else: # If never mod zero, then prime
                print ('prime')

is_prime(34)