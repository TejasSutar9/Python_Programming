OddNumber = lambda No : True if((No % 2) != 0) else False

def main():
    Value = int(input("Enter the number : "))
    
    Ret = OddNumber(Value)
    
    if(Ret == True):
        print(Value," is a Odd Number")
        
    else:
        print(Value," is a not an Odd Number")
        

if __name__ == "__main__":
    main()