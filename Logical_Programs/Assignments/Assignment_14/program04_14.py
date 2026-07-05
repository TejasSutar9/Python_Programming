Minimum = lambda No1,No2 : No1 if No1 < No2 else No2        # value_if_true if condition else value_if_false

def main():
    Value1 = int(input("Enter first number : "))
    
    Value2 = int(input("Enter second number : "))
    
    Ret = Minimum(Value1,Value2)
    
    print(Ret," is a minimum number")

    
if __name__ == "__main__":
    main()