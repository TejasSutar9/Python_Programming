# Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number.

def CheckGreater(No1,No2):
    if(No1 > No2):
        print("Greater Number is : ",No1)
        
    else:
        print("Greater Number is : ",No2)

def main():
    Value1 = 0
    Value2 = 0
    
    print("Enter first Number")
    Value1 = int(input())
    
    print("Enter second Number")
    Value2 = int(input())
    
    CheckGreater(Value1,Value2)

if __name__ == "__main__":
    main()