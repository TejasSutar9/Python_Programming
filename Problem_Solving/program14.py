def display_convert(cvalue):
    if cvalue == 'a':
        print('A')
    elif cvalue == 'D':
        print('d')


def main():
    print("Enter Character : ")
    cvalue = input()   

    display_convert(cvalue)


main()