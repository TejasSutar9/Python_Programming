def ReverseDigits(No):
    reverse = 0
    
    while(No != 0):
        Digit = No % 10
        reverse = (reverse * 10) + Digit
        No = No // 10

    return reverse


def main():
    Value = 0
    print("Enter the number : ")
    Value = int(input())
    
    Ret = ReverseDigits(Value)
    
    print("Reverse digits : ",Ret)
    
if __name__ == "__main__":
    main()