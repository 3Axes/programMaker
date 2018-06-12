import variables

def opt():
    ifloop = ''
    print()
    print('This module creates a logic loop (if/then/else).')
    print()

    ifloop += create() #creates the basic if statement

    cont = True
    while cont:
        addelif = input('Would you like to add an elif (then)? (y/n)\n') #checks if the user wants an elif
        if addelif.lower() == 'y':
            ifloop += elseif() #if they do, continue asking as well as add an elif
        else:
            ifloop += onlyelse() #if they don't, exit the loop by adding an else

            print('After exiting ProgramMaker, you can go and add code into these loops.')
            print('Editing the contents of an if loop is not supported... yet.')
            cont = False

    return ifloop #returns the entire built loop


def create():
    print('The if loop accepts a condition.')
    print('This can be an equation being true, or a variable being a certain value, etc.')
    print()
    print('All variables in your program:')
    print()

    variables.displayvars() #calls the displayvars function to get all variables explicitly defined

    print()

    condition = input('What condition would you like to use in your if loop? (Type the entire equation or equality symbol)\n')

    return "if %s:" % condition #fills in the command's shell with the info needed.

def elseif():
    print('The elif accepts a condition.')
    print('This can be an equation being true, or a variable being a certain value, etc.')
    print()
    print('All variables in your program:')
    print()

    variables.displayvars()

    print()

    condition = input('What condition would you like to yous in your elif loop? (Type the entire equation or equality symbol)\n')

    return '\nelif %s:' % condition #returns an elif with the \n to make sure the if and elifs don't overlap

def onlyelse():
    return '\nelse:' #return the else with the \n newline to avoid overlapping
