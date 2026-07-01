def SumNatural(No1):
    Sum = 0
    for i in range(1,No1+1):
        Sum = Sum + i
        
    return Sum

def main():
    Value = 0
    print("Enter the number : ")
    Value = int(input())
    
    Ret = SumNatural(Value)
    
    print("Sum of first ",Value," natural numbers : ",Ret)

if __name__ == "__main__":
    main()