EvenNumber = lambda No : ((No % 2) == 0) 

def main():
    Data = [10, 15, 20, 25, 30, 35]
    
    Result = list(filter(EvenNumber,Data))
    
    print("Original List : ",Data)
    print("Even List : ",Result)   
    
    
if __name__ == "__main__":
    main()