#This is the Collatz Sequence.
#This is commonly known as "the simplest impossible math problem."
#Authored by Kyle Z
#I forgot to add a comment, so i created a branch in git."
#Ugg...more stupid comments for the sake of Git.


def collatz(numb):
    if numb % 2 == 0:
        return numb//2
    else:
        return numb*3 + 1

def redone(usernumb):
    while usernumb!=1:
        display = collatz(usernumb)
        print(display)
        usernumb = display

userinput = 0
print('Welcome To Collatz')
print('Please type the number on which you wish to perform the Collatz sequence')
print('Type "exit" to exit')
while True:
    userinput = input()
    if userinput == 'exit' :
        break
    if userinput == str(0) :
        print('Please type a number >= 1')
        continue
    if userinput == '':
        continue
    redone(int(userinput))
