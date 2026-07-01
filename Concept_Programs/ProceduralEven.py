def CheckEven(No):
    if((No % 2) == 0):
        print("It is Even Number")
        
    else:
        print("It is Odd Number")


def main():
    Value = int(input("Enter Number : "))       # Dual task execution function
    
    CheckEven(Value)

if __name__ == "__main__":
    main()