def BigBazar():
    print("Inside BigBazar")
    
    def Amul():
        print("Inside Amul IceCream Parlour")

def main():
    BigBazar()                   # Allowed
    Amul()                       # Error
    BigBazar.Amul()              # Error

if __name__ == "__main__":
    main()