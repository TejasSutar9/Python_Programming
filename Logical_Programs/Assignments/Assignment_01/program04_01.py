# Write a program which accepts one number and prints cube of that number.

def Cube(No1):
    return No1 * No1 * No1

def main():
    print("Enter the number : ")
    Value = int(input())
    
    Result = Cube(Value)
    print("Cube of the number is : ",Result)

if __name__ == "__main__":
    main()