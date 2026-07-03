def CheckVowel(Char):
    if(Char == 'a' or Char == 'e' or Char == 'i' or Char == 'o' or Char == 'u' or
       Char == 'A' or Char == 'E' or Char == 'I' or Char == 'O' or Char == 'U'):
        return True
    else:
        return False


def main():
    Value = ""

    print("Enter a character : ")
    Value = input()

    Ret = CheckVowel(Value)

    if(Ret == True):
        print("It is a Vowel")
    else:
        print("It is a Consonant")


if __name__ == "__main__":
    main()