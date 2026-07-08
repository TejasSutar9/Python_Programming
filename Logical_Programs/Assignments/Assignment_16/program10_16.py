def StringLength(Str1):
    Count = 0
    
    for ch in Str1:
        Count = Count + 1
        
    return Count


def main():
    Str = ""
    print("Enter String : ")
    Str = input()
    
    Ret = StringLength(Str)
    
    print("String Length is : ",Ret)
        
    
if __name__ == "__main__":
    main()