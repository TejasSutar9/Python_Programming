from functools import reduce

Minimum = lambda No1,No2 : No1 if No1 < No2 else No2

def main():
    Data = [11, 21, 111, 51, 101]
    
    Result = reduce(Minimum,Data)
    
    print("Original List : ",Data)
    print("Minimum using reduce : ",Result)
    
if __name__ == "__main__":
    main()