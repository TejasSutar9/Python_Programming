DivisibleBy3and5 = lambda No : (((No % 3) == 0) and ((No % 5) == 0))

def main():
    Data = [3, 5, 15, 25, 30, 37, 45]
    
    Result = list(filter(DivisibleBy3and5, Data))
    
    print("Original List : ",Data)
    print("Divisible by 3 and 5 List : ",Result)   
    
    
if __name__ == "__main__":
    main()