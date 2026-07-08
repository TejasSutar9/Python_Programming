import Arithematic

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))
    
    print("Addition is : ",Arithematic.Add(Value1,Value2))
    print("Substraction is : ",Arithematic.Sub(Value1,Value2))
    print("Multiplication is : ",Arithematic.Mult(Value1,Value2))
    print("Division is : ",Arithematic.Div(Value1,Value2))
    
if __name__ == "__main__":
    main()