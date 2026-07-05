square = lambda No : No * No

def main():
    Data = [1, 2, 3, 4, 5]
    
    Result = list(map(square,Data))
    
    print("Original List : ",Data)
    print("Square List : ",Result)   
    
    
if __name__ == "__main__":
    main()