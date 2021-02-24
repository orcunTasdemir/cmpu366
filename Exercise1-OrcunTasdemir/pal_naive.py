


exp = input("Check whether your word is a palindrome!: ")

print("Your word you have given is: " + exp)

if len(exp) <=2:
  print("Sorry, try something longer." )

else:
    reversedExp = exp[::-1]
    print(reversedExp)
    if exp == reversedExp:
      print("Yes.'" + exp + "' is a palindrome.")
    else:
      print("No.'" + exp + "' is not a palindrome.")


