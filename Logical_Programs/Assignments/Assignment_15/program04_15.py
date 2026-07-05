from functools import reduce

Addition = lambda No1,No2 : No1 + No2

def main():
    Data = [1, 2, 7, 4, 5, 9]
    
    Result = reduce(Addition,Data)
    
    print("Original List : ",Data)
    print("Addition of all elements using reduce : ",Result)
    
if __name__ == "__main__":
    main()