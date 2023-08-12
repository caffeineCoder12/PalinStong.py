#Armstrong number
#Eg : 371


def armstrongNum():
    
    n = int(input("Enter a number "))
    nst = str(n)
    l = len(nst)
    ln = list(nst)

    a = 0

    for i in (ln):
        exp = int(i)**int(l)
        a += exp
    
    if a == n:
        print(n,"is an armstrong number")

    else:
        print(n,"is not an armstrong number")
        
armstrongNum()
    
while True:
    opt = input("Press y to continue and any other key to exit. ")
    if opt.lower() == "y":
        armstrongNum()
    else:
        print("\nGoodbye!")
        break
