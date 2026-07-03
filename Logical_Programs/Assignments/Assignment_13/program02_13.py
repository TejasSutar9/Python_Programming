def AreaCircle(Radius):
    Area = 3.14 * Radius * Radius
    return Area


def main():
    Radius = 0

    print("Enter the radius : ")
    Radius = float(input())

    Ret = AreaCircle(Radius)

    print("Area of Circle :", Ret)


if __name__ == "__main__":
    main()