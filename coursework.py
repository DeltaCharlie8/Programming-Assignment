# This program will implement an FSA to accept the string "ABACCB".

word = input("Enter a string: ")        #Asks the user to input a string
state = 1

for c in (word):
    if state == 1 and c == 'C':
        state = 1
    elif state == 1 and c == 'A':
        state = 2
    elif state == 2 and c == 'B':
        state = 3
    elif state == 2 and c == 'A':
        state = 1
    elif state == 3 and c == 'A':
        state = 4
    elif state == 4 and c == 'A':
        state = 4
    elif state == 4 and c == 'B':
        state = 3
    elif state == 4 and c == 'C':
        state = 5
    elif state == 5 and c == 'C':
        state = 6
    elif state == 6 and c == 'A':
        state = 5
    elif state == 6 and c == 'B':
        state = 7
    elif state == 6 and c == 'C':
        state = 6
    elif state == 7 and c == 'C':
        state = 5
    elif state == 7 and c != 'C':
        state = 8
    else:
        state = 8
    
if state == 7:
    print ("True.")
    print ("Goodbye.")
else:
    print ("False.")
    print ("Goodbye.")