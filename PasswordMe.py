#   Joshua Wells
#   PasswordMe - A simple password generator
#   Last edit: 09/18/2023

import random

def main():
    #   Prompts for password length, to include special characters, and to include numbers.
    passLen = int(input("How long would you like your password to be? (Please input a positive integer): "))
    specChars = input("Would you like to use special characters? (Enter 'y' or 'n' for yes or no respectively): ")
    useNums = input("Would you like to use numbers? (Enter 'y' or 'n' for yes or no respectively): ")
    password = ""
    
    password = generatePassword(passLen, specChars, useNums)
    
    print(password)


def generatePassword(passLen, specChars, useNums):
    #   Lists for all possible characters (lowercase and uppercase),
    #   numbers, and special characters that can be used for passwords.
    charsList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upperCharsList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    specCharsList = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*']
    numList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    passwordList = []
    passwordStr = ""
    
    temp = 0
    
    #   Loops for the length of the desired password
    for x in range(passLen):
        #   Loops while a character has not yet been
        #   concatenated to the password
        while(temp != 1):
            #   If special characters may be added, generate a random
            #   number between 0 and 1 to determine if the special
            #   character will be added.
            if(specChars == "y"):
                if(random.randint(0, 1) == 1):
                    passwordList.append(specCharsList[random.randint(0, len(specCharsList) - 1)])
                    temp += 1
            if(temp == 0):  #   If a character has still not been added
                if(useNums == "y"): #   Same process as with special characters
                    if(random.randint(0, 1) == 1):
                        passwordList.append(numList[random.randint(0, len(numList) - 1)])
                        temp += 1
            if(temp == 0):  #   Character still not added
                if(random.randint(0, 1) == 1):  #   Same process again
                    passwordList.append(upperCharsList[random.randint(0, len(upperCharsList) - 1)])
                    temp += 1
                else:   #   If the end is reached and no characters are added, add a lowercase letter
                    passwordList.append(charsList[random.randint(0, len(charsList) - 1)])
                    temp += 1
        temp = 0

    #   Concatenates all elements of passwordList into one string
    for i in range(len(passwordList)):
        passwordStr += passwordList[i]
    
    #   Returns string to main
    return str(passwordStr)
        
main()
