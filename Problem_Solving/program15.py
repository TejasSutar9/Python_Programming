def CheckVowel(CValue):
    if(CValue == 'a' or CValue == 'e' or CValue == 'i' or CValue == 'o' or CValue == 'u' or CValue == 'A' or CValue == 'E' or CValue == 'I' or CValue == 'O' or CValue == 'U'):
        return True
    else:
        return False

def main():
    print("Enter Character : ")
    cvalue = input()

    bRet = CheckVowel(cvalue)

    if(bRet == True):
        print("It is a vowel")
    else:
        print("It is not a vowel")
    
main()