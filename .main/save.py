#save module

def save(obj, path):
    print('Writing...')
    with open(path, 'w+') as file: #opens the file specified as 'file'
        file.write(obj) #writes the corresponding object into the file
    file.close() #closes the file
    print('Save complete.')
    exit() #exits the program

def load(path):
    import programMaker #if this is imported at the beginning, it causes errors
    print('Opening...')
    with open(path, 'r+') as file: #reads file, gets content
        content = file.read()
    file.close()
    print('Loaded.')
    programMaker.start(content, path) #sends content to the main instance, where it adds it to programMaker's final.
