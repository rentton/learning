import sys

def CorrectOrder(S):
    for i in range(len(S)):
        for j in range(i,len(S)):
            if S[j] < S[i]:
                return 0
    return 1

def Count(S):
    result = [0,0,0];
    for i in range(len(S)):
        if S[i] == 'a':
            result[0] += 1
        elif S[i] == 'c':
            result[1] += 1
        elif S[i] == 'b':
            result[2] += 1
    return result
        

def LexicalAnalizer(S):
    if S[0] != 'a':
        #print("1")
        return 0
    elif not CorrectOrder(S):
        #print("2")
        return 0
    else:
        letters = Count(S);
        if letters[0] >= 3 and letters[1] >= 0 and letters[2] == 0:
            return 1
        elif letters[0] >= 1 and letters[0] < 3 and letters[1] == 0 and letters[2] >= 0:
            return 1
        else:
            #print(f"{letters[0]}-{letters[1]}-{letters[2]}")
            return 0
      
      
if len(sys.argv) != 2:
    print("You must write a string. " +
          "Run again: python3 lexicalAnalizer.py [string]")
else:
    print(f"{sys.argv[1]}:")
    if LexicalAnalizer(sys.argv[1]) == 1:
        print("\tYes")
    else:
        print("\tNo")
        
# L = { aibj: 1<=i<3, j>=0} U {aic^j: i>= 3, j>=0} 	
        