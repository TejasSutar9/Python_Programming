Divisible = lambda No : True if((No % 5) == 0) else False

def main():
    Value = int(input("Enter the number : "))
    
    Ret = Divisible(Value)
    
    if(Ret == True):
        print(Value," is divisible by 5")
        
    else:
        print(Value," is not divisible by 5")
        

if __name__ == "__main__":
    main()