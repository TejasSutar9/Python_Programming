def CheckPerfect(No1):
    Sum = 0

    for i in range(1, No1):
        if(No1 % i == 0):
            Sum = Sum + i

    if(Sum == No1):
        return True
    else:
        return False


def main():
    Value = 0

    print("Enter the number : ")
    Value = int(input())

    Ret = CheckPerfect(Value)

    if(Ret == True):
        print("Perfect Number")
    else:
        print("Not a Perfect Number")


if __name__ == "__main__":
    main()