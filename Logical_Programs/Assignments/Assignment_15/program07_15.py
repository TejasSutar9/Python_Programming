LengthGreaterThan5 = lambda Str: len(Str) > 5

def main():
    Data = ["Apple", "Banana", "Mango", "Orange", "Kiwi", "Pineapple"]

    Result = list(filter(LengthGreaterThan5, Data))

    print("Original List :", Data)
    print("Filtered List :", Result)

if __name__ == "__main__":
    main()