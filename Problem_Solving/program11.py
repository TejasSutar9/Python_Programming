def PrintEven(No):
    if(No <= 0):
        return
    
    for i in range(1,No+1):
        print(2*i, end=" ")
            

def main():

    value = 0

    print("Enter Number : ")
    value = int(input())

    PrintEven(value)
    
main()