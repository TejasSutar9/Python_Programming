import MarvellousNum

def ListPrime(Data):
    Sum = 0

    for Value in Data:
        if(MarvellousNum.ChkPrime(Value) == True):
            Sum = Sum + Value

    return Sum


def main():
    Size = int(input("Enter the number of elements : "))

    Data = []

    print("Enter the elements :")

    for i in range(Size):
        No = int(input())
        Data.append(No)

    Ret = ListPrime(Data)

    print("Addition of all prime numbers :", Ret)


if __name__ == "__main__":
    main()