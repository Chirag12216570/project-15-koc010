p=int(input("ENTER THE STARTING RANGE "))
q=int(input("ENTER THE ENDING RANGE "))
for a in range(p,q+1):
    if a>1:
        for i in range(2,int(a/2)+1):
                if a%i==0:
                    print(a," is a composite number")
                    break
        else:   
            print(a," is a prime number")
    else:
        print(a,"is a composite number")
