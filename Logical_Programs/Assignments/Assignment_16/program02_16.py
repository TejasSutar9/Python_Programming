def CheckNum(No):
    if((No % 2) == 0):
        return True
    
    else:
        return False


def main():
    Value = 0
    print("Enter Number : ")
    Value = int(input())
    
    Ret = CheckNum(Value)
    
    if(Ret == True):
        print("Even Number")
        
    else:
        print("Odd Number")
    
    
if __name__ == "__main__":
    main()