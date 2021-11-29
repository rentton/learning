import sys

def LexicalAnalizer(L):
    if L[0] != 'a' or L[len(L)-1] != 'c':
        return False
    else:
        for i in range(1,len(L)-1):
            if L[i] < L[i-1]:
                return False
        return True
    
if (len(sys.argv) != 2):
    print("You must write a string. " +
          "Run again: python3 lexicalAnalizer.py [string]")
else:
    print(f"{sys.argv[1]}:")
    if LexicalAnalizer(sys.argv[1]):
        print("\tYes")
    else:
        print("\tNo")
