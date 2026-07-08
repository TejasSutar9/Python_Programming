def Divisible(No):
    if((No % 5) == 0):
        return True
    
    else:
        return False
    

def main():
    Value = 0
    print("Enter number : ")
    Value = int(input())
    
    Ret = Divisible(Value)
    
    if(Ret == True):
        print("True")
        
    else:
        print("False")
    

if __name__ == "__main__":
    main()