def CountDigits(No):
    Count = 0
    
    while(No != 0):
        Digit = No % 10
        No = No // 10
        Count = Count + 1
        
    return Count

def main():
    Value = 0
    print("Enter the number : ")
    Value = int(input())
    
    Ret = CountDigits(Value)
    
    print("count of digits : ",Ret)
    

if __name__ == "__main__":
    main()