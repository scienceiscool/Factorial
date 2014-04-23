#!/my-computer's-name/bin/python

#Kathy Saad

def printInts(maxcount):
    print range(1, maxcount+1)

def printFactorial(inputvalue):
    n = 1

    exclam = "! = "

    print inputvalue, exclam,

    while inputvalue >= 1:
          n = n * inputvalue
          
          if inputvalue > 1:
             print inputvalue, " * ",
          else:
             print inputvalue,

          inputvalue = inputvalue - 1

    print " also known as ", n;

def getInt():
    inputval = input("Enter a positive integer value:")
    
    if inputval < 0:
       inputagain = input("Re-enter the value; it must be a positive integer.")

       while inputagain < 0:
             inputagain = input("Re-enter the value; it must be a positive integer.")
    
    elif inputval > 5:
       printInts(inputval)

    else:
         print printFactorial(inputval)

getInt()
