def Accept(No):

    if(No < 0):         #updater
        No = -No

    for i in range(1, No + 1):
        print("*",end=" ")

def main():
    value = 0

    print("Enter Number : ")
    value = int(input())

    Accept(value)    

main()