def Divisibleby5(No):
    if(No % 5 == 0):
        print("It is divisible by 5")
    else:
        print("It is not divisible by 5")

def main():
    value = 0

    print("Enter Number : ")
    value = int(input())

    Divisibleby5(value)    

main()