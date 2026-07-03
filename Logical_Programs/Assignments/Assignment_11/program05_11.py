def PalindromeNumber(No):
    Temp = No
    reverse = 0
    
    while(No != 0):
        Digit = No % 10
        reverse = (reverse * 10) + Digit
        No = No // 10
        
    if(Temp == reverse):
        return True
    
    else:
        return False
    

def main():
    Value = 0
    print("Enter the number : ")
    Value = int(input())
    
    Ret = PalindromeNumber(Value)
    
    if(Ret == True):
        print("It is palindrome number")
        
    else:
        print("It is not palindrome number")    
    

if __name__ == "__main__":
    main()