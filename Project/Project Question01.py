def dictionary():##function that loads morse code from file into a dictionary
    global d
    file = open("morse.txt", "r")
    file = file.readlines()
    d ={}
    a = " "
    b = ""
    for i in file:
        i = i.split()##creating list of elements
        d[i[0]] = i[1]## i at index 0 = key, i at index 1 = value
        d[" "] = " "##spaces added for space recognition in decoding function
        d[""] = ""
    

    def menu():##menu function, prints menu
        print("")
        print("\nHello, this program allows you to translate text to morse code or translate morse code to text")
        print("Please, select one of the below options:")
        print("*** Enter 't' for encoding text")
        print("*** Enter 'm' for decoding morse code")
        print("*** Enter 'e' to exit the program")
        print("")
        
    def encoding():##function that converts normal text to morse code
        line = input("Please enter text to translate\n")
        line = line.upper()
        L = line.split()
        for words in L:
            words.split()
            for e in words:
                print(d.get(e),"", end = "")##getting the value associated to key
            print("   ", end = "")
    def decoding():##function that converts morse code to english language
        global d
        line = input("Please enter morse to translate:\n")
        L = line.split("   ")
        a = []
        for e in L:
            a = e.split(" ")
            for i in a:
                ##getting the keys based off the values
                print(list(d.keys())[list(d.values()).index(i)], end = "")
            print(" ", end = "")
     
    def mainfunction():##function for the main part of the program
        menu()
        x = input("My input is:")
        while x != 'e':##breaks out of while loop if input is e
            if x == 't':
                encoding()
                menu()
                x = input("My input is:")
            if x == 'm':
                decoding()
                menu()
                x = input("My input is:")
            while x != 't' and x != 'm' and x != 'e':##validating user input
                print("")
                print("*** invalid option")
                x = input("Please enter a valid option\n")
                print("")
        print("")
        print("Thanks for using this program!")##outside of while loop
    mainfunction()

dictionary()
