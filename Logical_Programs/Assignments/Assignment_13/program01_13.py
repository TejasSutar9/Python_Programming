def AreaRectangle(Length, Width):
    Area = Length * Width
    return Area


def main():
    Length = 0
    Width = 0

    print("Enter the length : ")
    Length = float(input())

    print("Enter the width : ")
    Width = float(input())

    Ret = AreaRectangle(Length, Width)

    print("Area of Rectangle :", Ret)


if __name__ == "__main__":
    main()