def CheckEven(No):
    if(No % 2 == 0):
        print("It is even number")
    else:
        print("It is odd number")

def main():
    value = 0

    print("Enter Number : ")
    value = int(input())

    CheckEven(value)    

main()