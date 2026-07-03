def Arithmetic(No1, No2):
    print("Addition :", No1 + No2)
    print("Subtraction :", No1 - No2)
    print("Multiplication :", No1 * No2)
    print("Division :", No1 / No2)


def main():
    Value1 = 0
    Value2 = 0

    print("Enter first number : ")
    Value1 = int(input())

    print("Enter second number : ")
    Value2 = int(input())

    Arithmetic(Value1, Value2)


if __name__ == "__main__":
    main()