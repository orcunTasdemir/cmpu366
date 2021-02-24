


###Fucntion Definitions

def get_rev(string):
    return string[::-1]

punctuation = ('!','.',':',';','"',',','`','~',"'",'?','/',']','[','{','(',')','-','_')

def clean_input(string):
    string = ''.join(string.lower().split())
    string = ''.join(c for c in string if c not in punctuation)
    return string