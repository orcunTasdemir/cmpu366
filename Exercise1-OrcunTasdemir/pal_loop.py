from functions import clean_input
from functions import get_rev


print("Hello, Let's start!")

noPalindromes = True


while noPalindromes == True:

    originalExp = input("Give me a palindrome: ")

    #print("Your word you have given is: " + originalExp)

    exp = clean_input(originalExp)
    
    print(exp)

    if len(exp) <=2:
        print("Sorry, try something longer." )

    else:
        reversedExp = get_rev(exp)
        #print(reversedExp)
        if exp == reversedExp:
            print("Yes.'" + originalExp + "' is a palindrome. Goodbye.")
            noPalindromes = False
        else:
            print("No.'" + originalExp + "' is not a palindrome. Let's try again.")

  


