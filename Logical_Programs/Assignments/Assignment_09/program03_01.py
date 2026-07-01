# Write a program which accepts one number and prints square of that number.

def square(No1):
    return No1 * No1

def main():
    print("Enter the number : ")
    Value = int(input())
    
    Result = square(Value)
    print("Square of the number is : ",Result)

if __name__ == "__main__":
    main()