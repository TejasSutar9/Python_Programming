def Maximum(Data):
    Max = Data[0]

    for Value in Data:
        if(Value > Max):
            Max = Value

    return Max


def main():
    Size = int(input("Enter the number of elements : "))

    Data = []

    print("Enter the elements :")

    for i in range(Size):
        No = int(input())
        Data.append(No)

    Ret = Maximum(Data)

    print("Maximum number is :", Ret)


if __name__ == "__main__":
    main()