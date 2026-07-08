def DisplayReverse(No):
    print("Reverse Numbers : ")
    for i in range(No, 0, -1):
        print(i)

def main():
    Value = 0
    print("Enter Number : ")
    Value = int(input())
    
    DisplayReverse(Value)
    
if __name__ == "__main__":
    main()