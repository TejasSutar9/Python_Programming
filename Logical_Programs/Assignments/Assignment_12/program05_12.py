def DisplayReverse(No1):
    for i in range(No1, 0, -1):
        print(i)


def main():
    Value = 0

    print("Enter the number : ")
    Value = int(input())

    DisplayReverse(Value)


if __name__ == "__main__":
    main()