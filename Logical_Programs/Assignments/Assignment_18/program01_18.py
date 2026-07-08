def Addition(Data):
    Sum = 0

    for Value in Data:
        Sum = Sum + Value

    return Sum


def main():
    Size = int(input("Enter the number of elements : "))

    Data = []

    print("Enter the elements :")

    for i in range(Size):
        No = int(input())
        Data.append(No)

    Ret = Addition(Data)

    print("Addition of all elements :", Ret)


if __name__ == "__main__":
    main()