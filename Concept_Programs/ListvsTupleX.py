#------------------------------------
#                   List     Tuple
#------------------------------------
# Ordered           Yes      Yes
# Indexed           Yes      Yes
# Mutable           Yes      No
# Heterogenous      Yes      Yes
#------------------------------------

def main():
    
    Data1 = [10,3.14,True,"pune"]       # List
    Data2 = (10,3.14,True,"pune")       # Tuple
    
    print(Data1)
    print(Data2)
    
    print(Data1[0])
    print(Data2[0])
    
if __name__ == "__main__":
    main()