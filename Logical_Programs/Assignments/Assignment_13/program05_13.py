def DisplayGrade(Marks):
    if(Marks >= 75):
        print("Distinction")
    elif(Marks >= 60):
        print("First Class")
    elif(Marks >= 50):
        print("Second Class")
    else:
        print("Fail")


def main():
    Value = 0

    print("Enter the marks : ")
    Value = int(input())

    DisplayGrade(Value)


if __name__ == "__main__":
    main()