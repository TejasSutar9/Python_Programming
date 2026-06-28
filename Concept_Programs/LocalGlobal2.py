no = 11             # Global Variable

def Display():
    a = 21          # Local Varibale
    print("From display : ",no)
    print("From display value of a is : ",a)

def Demo():
    print("From demo value of a is : ",a)       # Error
    print("From demo : ",no)
    pass

Display()
Demo()
