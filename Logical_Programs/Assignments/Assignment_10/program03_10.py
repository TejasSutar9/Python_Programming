def Factorial(No1):
    Fact = 1
    for i in range(1,No1+1):
        Fact = Fact * i
        
    return Fact
    

def main():
    Value = 0
    print("Enter the number : ")
    Value = int(input())
    
    Ret = Factorial(Value)
    
    print("Factorial is : ",Ret)
    

if __name__ == "__main__":
    main()