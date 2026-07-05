square = lambda No : No * No

def main():
    Value = int(input("Enter the number : "))
    
    Ret = square(Value)
    
    print("Square is : ",Ret)
    
if __name__ == "__main__":
    main()