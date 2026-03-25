def Display(No):

    if(No < 10):
        print("Hello")
    else:
        print("Demo") 

        

def main():
    value = 0

    print("Enter Number : ")
    value = int(input())

    Display(value)    

main()