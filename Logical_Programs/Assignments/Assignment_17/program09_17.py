def CountDigits(No):
    if(No == 0):
        return 1
    
    Count = 0
    
    while(No != 0):
        No = No // 10
        Count = Count + 1
        
    return Count


def main():
    Value = int(input("Enter Number : "))
    
    Ret = CountDigits(Value)
    
    print("NUmber of digits : ",Ret)
    
if __name__ == "__main__":
    main()