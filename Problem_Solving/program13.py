def display_factor(no):
    if no <= 0:
        no = -no

    for i in range(1, no // 2 + 1):
        if(no % i == 0 and i % 2 == 0):
            print(i, end=" ")

def main():
    value = 0

    print("Enter Number : ")
    value = int(input())

    display_factor(value)
    
main()