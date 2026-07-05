OddNumber = lambda No : ((No % 2) != 0) 

def main():
    Data = [10, 11, 12, 13, 14, 15, 16, 17]
    
    Result = list(filter(OddNumber,Data))
    
    print("Original List : ",Data)
    print("Odd List : ",Result)   
    
    
if __name__ == "__main__":
    main()