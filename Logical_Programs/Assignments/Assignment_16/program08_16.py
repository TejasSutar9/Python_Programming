def Printt(No):
    for i in range(1,No+1):
        print("*",end=" ")


def main():
    Value = 0
    print("Enter Number : ")
    Value = int(input())
    
    Printt(Value)
    
if __name__ == "__main__":
    main()