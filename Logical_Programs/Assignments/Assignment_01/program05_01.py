# Write a program which accepts one number and checks whether it is divisible by 3 and 5

def CheckDivisibleby3and5(No1):
    if(((No1 % 3) == 0) and ((No1 % 5) == 0)):
        return True
    else:
        return False
    

def main():
    Value = 0
    print("Enter the Number : ")
    Value = int(input())
    
    Ret = CheckDivisibleby3and5(Value)
    
    if(Ret == True):
        print("It is divisible by 3 and 5")
        
    else:
        print("It is not divisible by 3 and 5")
            
    
if __name__ == "__main__":
    main()
