strinG = input("Enter a string:")
vowels = "aeiouy"
vowels2 = "AEIOUY"
cons = "bcdfghjklmnpqrstvwxz"
cons2 = "BCDFGHJKLMNPQRSTVWXZ"

def function1(strinG):
    vowel_count = 0
    for i in range (len(strinG)):
        if strinG[i].isalpha():
            if strinG[i] in vowels:
                vowel_count += 1
            elif strinG[i] in vowels2:
                vowel_count += 1
    print("The string you entered includes ", vowel_count," vowels and ", end= '')
def function2(strinG):
    cons_count = 0
    for i in range (len(strinG)):
        if strinG[i].isalpha():
            if strinG[i] in cons:
                cons_count += 1
            elif strinG[i] in cons2:
                cons_count += 1
    print(cons_count, " consonants.")
function1(strinG)
function2(strinG)

