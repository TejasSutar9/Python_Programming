from functools import reduce

Product = lambda No1, No2: No1 * No2

def main():
    Data = [2, 3, 4, 5]

    Result = reduce(Product, Data)

    print("Original List :", Data)
    print("Product of all elements :", Result)

if __name__ == "__main__":
    main()