def Minimum(Data):
    Min = Data[0]

    for Value in Data:
        if(Value < Min):
            Min = Value

    return Min


def main():
    Size = int(input("Enter the number of elements : "))

    Data = []

    print("Enter the elements :")

    for i in range(Size):
        No = int(input())
        Data.append(No)

    Ret = Minimum(Data)

    print("Minimum number is :", Ret)


if __name__ == "__main__":
    main()