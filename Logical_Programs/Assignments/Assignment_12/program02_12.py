def Factors(No1):
    for i in range(1, No1 + 1):
        if(No1 % i == 0):
            print(i)


def main():
    Value = 0

    print("Enter the number : ")
    Value = int(input())

    print("Factors are :")
    Factors(Value)


if __name__ == "__main__":
    main()