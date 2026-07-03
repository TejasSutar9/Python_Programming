def Display(No1):
    for i in range(1, No1 + 1):
        print(i)


def main():
    Value = 0

    print("Enter the number : ")
    Value = int(input())

    Display(Value)


if __name__ == "__main__":
    main()