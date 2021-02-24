
punctuation = ('!','.',':',';','"',',','`','~','?','/',']','[','{','(',')','-','_',"'")

originalExp = input("Check whether your word is a palindrome!: ")

print("Your word you have given is: " + originalExp)


exp = ''.join(originalExp.lower().split())
exp = ''.join(c for c in exp if c not in punctuation)

if len(exp) <=2:
  print("Sorry, try something longer." )

else:
    reversedExp = exp[::-1]
    #print(reversedExp)
    if exp == reversedExp:
      print("Yes.'" + originalExp + "' is a palindrome.")
    else:
      print("No.'" + originalExp + "' is not a palindrome.")


