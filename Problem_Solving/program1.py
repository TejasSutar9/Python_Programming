def Division(No1,No2):

    if No2 == 0:
        print("Not divisible by zero")
        return None

    if No2 > No1:
        return -1

    return No1 // No2

def main():
    value1 = 0
    value2 = 0

    print("Enter first number : ")
    value1 = int(input())

    print("Enter second number : ")
    value2 = int(input())

    Ret = Division(value1,value2)

    print("Division is : ",Ret)

main()