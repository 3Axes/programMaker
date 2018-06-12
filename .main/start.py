import programMaker as p #imports it for the start firstrun instance
import save as s

print('Welcome to ProgramMaker')

try: #gets the objective - load or create
    go = int(input("""What would you like to do?
    1: Create a new program
    2: Load a program to edit
    2: Exit
    Enter the number of your selection here: """))
except:
    print('An error occurred. Please try again later.')
    exit() #kills program if an exception occurs

if go == 1:
    filename = input('Enter the name of the file you are creating (or the desired filepath with the name(no extension)): ')
    filename += '.py' #adds .py to files to make them python accessible.
    p.start('', filename) #sends info to programMaker
elif go == 2:
    path = input('Please enter the path of the object you would like to open: ')
    s.load(path) #sends the path to save to get the info stored inside.
else:
    exit() #if nothing matches, exit the program
