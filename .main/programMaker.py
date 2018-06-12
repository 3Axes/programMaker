"""
@author: 3Axes
programMaker's main instance
"""
#imports all external modules.

import interactions
import variables
import loops
import logic
import save


version = '0.9.1'

final = """#Created using ProgramMaker v"""
final += str(version) #creates the version comment at the beginning of the created file

filepath = ''

loop = False

finaladd = '' #used for indent menu, not used now.
tab = """        """ #used for the indent menu, but not used now.

def displaycode():
    print(final) #mini-function to display all code created.

def indentor(param):
    if loop:
        return '\n' + tab + param
    else:
        return '\n' + param

def start(content, path): #initializes all of the starting variables necessary for loading or creating a file.
    global final
    final += '\n' + content
    global filepath
    filepath = path

    print('To import packages, type "$input <package>"')
    menu() #starts the main instance

def menu():
    global final
    global filepath
    global loop
    print('\n\n\nOperation Complete.')
    print('\n\nAvailable Options:\n') #printing all options
    print("""
    1: User Interactions (print, input)
    2: Variable Operations (assign, change)
    3: Loop Operations (for, while)
    4: Logic Operations (if/then/else)
    5: View current code
    6: Save and Exit
    (More functions to come in later updates)

    If you are experienced with python, you can add a custom line using the prefix $

    Type !ver for version

    If you are in a loop, type '!exit' to exit the loop.
    """)
    try:
        choice = input('\nEnter your choice: ')

        if choice[0] == '$': #for custom line prompts
            final += '\n%s' % choice[1:]
            menu() #reruns menu to keep the menu active

        if choice.lower() == '!ver': #prints version info
            print('ProgramMaker v', version, ' FE', sep='')
            menu()
        if choice.lower() == '!exit':
            loop = False
            menu()


        choice = int(choice) #changes the type to an integer - try will pick up any exceptions
        if choice == 1: #checks for choice picked
            final += indentor(interactions.opt())
        elif choice == 2:
            final += indentor(variables.opt())
        elif choice == 3:
            final += indentor(loops.opt())
            loop = True
        elif choice == 4:
            final += indentor(logic.opt())
            loop = True
        elif choice == 5:
            displaycode() #runs the mini function if the user chooses to display the code
        elif choice == 6:
            save.save(final, filepath) #saves and quits inside save module.
    except:
        print('An error occurred.') #if the program catches an exception

    menu() #keeps menu instance going
