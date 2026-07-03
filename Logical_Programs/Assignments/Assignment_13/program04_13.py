def Binary(No1):
    BinaryNo = ""

    while(No1 != 0):
        Digit = No1 % 2
        BinaryNo = str(Digit) + BinaryNo
        No1 = No1 // 2

    return BinaryNo


def main():
    Value = 0

    print("Enter the number : ")
    Value = int(input())

    Ret = Binary(Value)

    print("Binary equivalent :", Ret)


if __name__ == "__main__":
    main()