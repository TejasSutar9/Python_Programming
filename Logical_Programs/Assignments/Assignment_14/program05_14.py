EvenNumber = lambda No : True if((No % 2) == 0) else False

def main():
    Value = int(input("Enter the number : "))
    
    Ret = EvenNumber(Value)
    
    if(Ret == True):
        print(Value," is a Even Number")
        
    else:
        print(Value," is a not an Even Number")
        

if __name__ == "__main__":
    main()