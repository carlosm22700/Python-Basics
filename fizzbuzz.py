# functions are defined useing the def keyword


def fizz_buzz(max_num):
    # code blocks are defind using
    # indentation after a :
    '''
    Loops through 1 up to max_num and prints message depending on evaluation of the integer
    '''

    for num in range(1, max_num + 1):
        if num % 3 == 0 and num % 5 == 0:
            # using string format method
            print('{} is FizzBuzz'.format(num))
        elif num % 3 == 0:
            # using newer f string approach
            print(f'{num} is Fizz')
        elif num % 5 == 0:
            print(f'{num} is Buzz')
        else:
            print(num)


fizz_buzz(31)
