"""
@author: 3Axes
interactions module, ProgramMaker v0.1
"""

import variables #uses this for displayvars

def opt():
    print()
    print('Available Options in Interactions:') #printing options
    print("""
    1: Send a message to the user (string, variable, or a combination of both)
    2: Recieve input from the user (string, float or integer) and set it to a variable
    """)

    try:
        choice = int(input('Enter the number of your choice: '))

    except:
        print('An error occurred. Returning to the main menu...') #if not an integer, return an error
        return ''

    if choice == 1:
        return send() #print statements
    elif choice == 2:
        return get() #input statemetns
    else:
        print('Please enter 1 or 2. returning to main menu...') #if number isn't 1 or 2
        return ''

def send(): #submenu
    print('This will print a message to the console.')
    print("""You can:
    1: Print a message
    2: Print a variable
    """)
    choic = int(input('Enter your choice here: '))

    if choic == 1:
        return sendprint()
    else:
        return sendvar()

def sendprint(): #sends a message to the user, utilizes print and prints a string
    print('This will print a message to the console when your program is running.')
    message = input('Enter your message here: ')
    return 'print("%s")' % message

def sendvar(): #uses print to send a variable. This time, displays the variables and doesn't add quotes
    print('Here is the list of variables you have in your program:')
    print()
    variables.displayvars()
    print()
    varSend = input('Which variable would you like to print?\n')
    return 'print(%s)' % varSend

def get(): #input submenu
    print('This will get user input from the console.')
    print("""You can:
    1: Get a number
    2: Get a string""")
    choic = int(input('Enter your choice here: '))
    if choic == 1:
        x = gNum()
        return x
    else:
        x = gStr()
        return x

def gNum(): #for recieving numbers - can then add int or float to change type.
    print('This will allow you to get a number from the user.')
    type = input('Would you like the user to be able to input Floating-Point numbers? (1.25, 2.8392)\n(y/n): ') #user's chocie
    if type.lower() == 'n':
        fType = 'int'
    else:
        fType = 'float'

    varname = input('What variable name do you want to assign this input to?\n')

    message = input('Enter the prompt for the user: ')
    return '%s = %s(input("%s"))' % (varname, fType, message) #returns an input statement

def gStr():
    print('This will allow you to get a string from the user.') #gets a string

    varname = input('What variable name to you want to assign this input to?\n')

    message = input('Enter the prompt for the user: ')
    return '%s = input("%s")' % (varname, message) #returns an input statement
