
def rep1(strinG, rep):
        new_string = ""
        for i in range (rep):
                new_string = new_string + strinG
                if rep < 1:
                        print(" ")
        print( strinG, " -> ", new_string)
rep1("hello", 3)
