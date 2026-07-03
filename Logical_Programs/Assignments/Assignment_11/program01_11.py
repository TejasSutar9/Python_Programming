def CheckPrime(No1):
    if(No1 <= 1):
        return False
    
    for i in range(2,No1):
        if((No1 % i) == 0):
            return False
        
    return True


def main():
    Value = 0
    print("Enter the number : ")
    Value = int(input())
    
    Ret = CheckPrime(Value)
    
    if(Ret == True):
        print(Value," is Prime Number")
        
    else:
        print(Value," is not Prime Number")
           

if __name__ == "__main__":
    main()