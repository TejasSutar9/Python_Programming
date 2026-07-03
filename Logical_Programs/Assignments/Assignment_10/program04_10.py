def EvenNumber(No1):
    print("Even numbers are : ")
    for i in range(1,No1 + 1):
        if((i % 2) == 0):
            print(i)

def main():
    Value = 0
    print("Enter the number : ")
    Value = int(input())
    
    EvenNumber(Value)
    

if __name__ == "__main__":
    main()