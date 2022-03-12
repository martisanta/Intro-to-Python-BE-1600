
def openfile():##function to load emails from file
    global d ##define global variable d to access in later functions
    f = open("file.txt", "r")
    d = {}
    try:##testing block of code for errors, in case the file is empty
        for i in f:
            i = i.split(":")##create list of elements in each line
        d[i[0]] = i[1]## key = i at index 0, value = i at index 1 in dictionary (d)
    except:##if there are errors, the code will skip this and continue to the next step
        for i in f:
            continue
    
        
def menu():##function to load menu
    print("")
    print("Menu")
    print("-----------------------------------")
    print("1.Look up an email adress")
    print("2.Add a new name and email address")
    print("3.Change an existing email address")
    print("4.Delete a name and email address")
    print("5.Quit the program")
    print("")
def lookitup():##function to look up person's email address
    z = input("Enter a name:")
    if z in d.keys():
        print("Name:", z)
        print("Email:", d.get(z))## get value associated to key (z)
    else:
        print("The specified name was not found")
def addnewname():##function to add new name
    j = input("Enter name:")
    if j not in d:
        k = input("Enter email address:")
        d[j] = k ## add new entry/ key value pair
        print("Information added")
    else:
        print("That name already exists")
def changeitup():##function to change an email address
    j = input("Enter name:")
    if j in d.keys():
        k = input("Enter new address:")
        d[j] = k
        print("Information updated!")
    else:
        print("Specified name was not found")
    
def deleteit():##function to delete a name and email address
    j = input("Enter name:")
    if j in d.keys():
        del d[j]## delete entry
        print("Information deleted")
    else:
        print("Specified name was not found")

def savefile():##function to save emails in file
    f = open("file.txt", "w")
    for j, k in d.items():
        f.write("%s:%s\n" % (j, k))## write j,k in file and format to string
        f.close()
    print("Information saved")    

def mainfunction():##function for main part of the program
    global d ##redefine global variable d inside function
    openfile()
    menu()
    x = int(input("Enter your choice:"))
    while x != 5:## while input is not 5, the loop will run
        if x == 1:
            lookitup()
            menu()
            x = int(input("Enter your choice:"))
        if x == 2:
            addnewname()
            menu()
            x = int(input("Enter your choice:"))
        if x == 3:
            changeitup()
            menu()
            x = int(input("Enter your choice:"))
        if x == 4:
            deleteit()
            menu()
            x = int(input("Enter your choice:"))
    savefile()##once the loop is broken (when x == 5), file will be saved
mainfunction()
