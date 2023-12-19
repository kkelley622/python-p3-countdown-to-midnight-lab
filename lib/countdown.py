from time import sleep

# your code goes here!
def countdown(number):
    while number >= 1:
        print(f'{number} SECOND(S)!')
        number -= 1
    else:
        print('HAPPY NEW YEAR!')
def countdown_with_sleep(number):
    while number:
        print(f'{number} SECOND(S)!')
        number -= 1
        sleep(1)
    print ('HAPPY NEW YEAR!')
