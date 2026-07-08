def CheckNumber(No):
    if(No > 0):
        print("Positive Number")
        
    elif(No < 0):
        print("Negative Number")
        
    else:
        print("Zero")

def main():
    Value = 0
    print("Enter number : ")
    Value = int(input())
    
    CheckNumber(Value)
    
    
if __name__ == "__main__":
    main()    