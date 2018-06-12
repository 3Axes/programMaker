#logic mod

import variables

def opt():
    print('Available Options:') #displays loop options
    print()
    print("""
    1: Create a FOR loop (only range is supported currently)
    2: Create a WHILE loop
    """)

    try:
        choice = int(input('Enter your choice here: '))
    except:
        print('An error occurred. Returning to the menu...')
        return ''

    if choice == 1:
        return loopFor() #uses the two different functions for loop creation -- calls them to get their output and returns it.
    elif choice ==2:
        return loopWhile()
    else:
        print('An error occurred. Returning to the menu...') #if the input is anything that isn't expected.
        return ''

def loopFor():
    print()

    counter = input('What variable should count the iterations?\n') #for <this parameter> in range()

    print('range() can iterate over variables as well as numbers.')

    print('\nAll variables in your program:')
    variables.displayvars()

    print()

    iterate = input('Please enter a value or variable to iterate over: ') #for in range(<this parameter>)

    return 'for %s in range(%s):' % (counter, iterate) #returns the shell of the code with the user's fill-ins placed inside it.

def loopWhile():
    print()

    print('A While loop can iterate over booleans or true/false values (which can be contained in a variable, if you\'ve created one.')
    print('A While loop can also iterate over an equation (i.e. as long as 1 == 1, etc.)')

    print()
    variables.displayvars()
    print()

    validator = input('Enter the variable, equation or t/f statement to iterate over: ') #gets a user's validator request and implements it.
    return 'while %s:' % str(validator)
