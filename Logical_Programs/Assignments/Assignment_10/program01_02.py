def MultiplicationTable(No1):
    for i in range(1,11):
        print(No1," x ",i," = ",No1*i)
    

def main():
    Value = 0
    print("Enter the number : ")
    Value = int(input())
    
    MultiplicationTable(Value)
    

if __name__ == "__main__":
    main()