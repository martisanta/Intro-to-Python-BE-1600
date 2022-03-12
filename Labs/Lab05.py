##strName.upper()


def function1():
    vowel = 0
    word = input("Enter a string")
    word = word.upper()
    new_word= ""
    print("Old string: ", word)
    for i in range (len(word)):
        if 'A' in word[i]:
            new_word = new_word + "*"
            vowel += 1
        elif 'E' in word[i]:
            new_word = new_word + "*"
            vowel += 1
        elif 'I' in word[i]:
            new_word = new_word + "*"
            vowel += 1
        elif 'O' in word[i]:
            new_word = new_word + "*"
            vowel += 1            
        elif "U" in word[i]:
            new_word = new_word + "*"
            vowel += 1
        else:
            new_word = new_word + word[i]
    print("New string: ", new_word)
    print("The number of vowels is ", vowel)
function1()


