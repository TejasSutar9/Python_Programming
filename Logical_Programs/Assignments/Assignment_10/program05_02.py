def OddNumber(No1):
    print("Odd numbers are : ")
    for i in range(1,No1 + 1):
        if((i % 2) != 0):
            print(i)

def main():
    Value = 0
    print("Enter the number : ")
    Value = int(input())
    
    OddNumber(Value)
    

if __name__ == "__main__":
    main()