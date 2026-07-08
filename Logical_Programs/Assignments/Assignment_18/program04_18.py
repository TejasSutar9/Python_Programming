def Frequency(Data, No):
    Count = 0

    for Value in Data:
        if(Value == No):
            Count = Count + 1

    return Count


def main():
    Size = int(input("Enter the number of elements : "))

    Data = []

    print("Enter the elements :")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Search = int(input("Enter the number to search : "))

    Ret = Frequency(Data, Search)

    print("Frequency of", Search, "is :", Ret)


if __name__ == "__main__":
    main()