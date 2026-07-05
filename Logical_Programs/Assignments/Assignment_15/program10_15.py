Even = lambda No: (No % 2) == 0

def main():
    Data = [10, 15, 20, 25, 30, 35, 40]

    Result = list(filter(Even, Data))

    print("Original List :", Data)
    print("Count of Even Numbers :", len(Result))

if __name__ == "__main__":
    main()