import gc

class Var: #creates the var class to define and store all variables
    def __init__(self, name, value):
        self.__name = name
        self.__value = value
        self.typecheck()

    def typecheck(self):
        try: #type-checking - puts type into self.__type
            if self.__value.isalnum():
                float(self.__value)

                if float(self.__value).is_integer():
                    self.__type = int
                    self.__value = int(self.__value)
                else:
                    self.__type = float
                    self.__value = float(self.__value)

        except:
            if self.__value[0] == '[':
                self.__type = list
                self.__value = list(self.__value)
            elif self.__value[0] == '(':
                self.__value = tuple(self.__value)
                self.__type = tuple
            elif self.__value == 'True' or self.__value == 'False':
                if self.__value == 'True':
                    self.__value = True
                else:
                    self.__value = False
                self.__type = bool
            else:
                self.__type = str

    def checktype(): #getters
        return self.__type
    def checkval(): #getters
        return self.__value
    def __str__(self): #prints the variable's status
        return '\n%s\n%s\nValue:%s' % (self.__name, str(self.__type), str(self.__value))
    def setval(self,valueChange): #changes the variable's value
        self.__value = valueChange
        self.typecheck()




def opt():
    print() #prints all the options
    print('Available Options:')
    print("""
    1: Create a variable (x = 5)
    2: Change a variable (change the value of x later in the program)
    3: See all variables (view values and types)
    """)
    try:
        choice = int(input('Please enter the number of your choice: '))
    except:
        print('An error occurred. Returning to the main menu...')
        return ''

    if choice == 1: #checks for choice
        fin = create()
        return fin
    elif choice == 2:
        fin = change()
        return fin
    elif choice == 3:
        displayvars()
        return ''
    else:
        print('Please enter a number between 1 and 3. Returning to main menu...')
        return ''




def create(): #tells the user what options are available in the subloop
    print("""Change the VALUE To Create:
        An integer - simply type the number
        A string - just type the string
        A list - the first character has to be '[', last character ']', values separated with ','
        A tuple - the first character has to be '(', last character has to be ')', values separated with ','
        A boolean - type 'True' or 'False' - capitalization matters
        """)
    name = input('Enter the name of the variable you want to create: ')
    value = input('Enter the value of the variable you want to create: ')
    globals()[name] = Var(name, value) #using globals(), creates a variable with the name the user sets as the Var() object
    print('Variable Created.')
    msg = '\n' + name + ' = ' + value
    return '%s = %s' % (name, value) #returns the variable creation string



def change():
    print('All variables in your program: ')
    print()
    displayvars()
    print()
    name = input('Enter the name of the variable you want to change: ')
    value = input('Enter the value of the variable you want to change: ')
    try:
        globals()[name].setval(value) #uses the globals function to use the setvar function of the variable the user selects.
    except: #if the variable doesn't exist:
        print('\n\nError:')
        print('That variable was not found.')
        return ''
    print('Variable Changed.')
    return '%s = %s' % (name, value)




def displayvars(): #uses garbage collector to collect all objects in program
    for obj in gc.get_objects():
        if isinstance(obj, Var): #for every object that is Var (all of them)
            print(obj) #calls the __str__ method
