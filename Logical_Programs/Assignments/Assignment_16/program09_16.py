def PrintEven(No):
    for i in range(2,No+1,2):
        print(i,end=" ")

def main():
    Value = 0
    print("Enter Number : ")
    Value = int(input())
    
    PrintEven(Value)
    
if __name__ == "__main__":
    main()