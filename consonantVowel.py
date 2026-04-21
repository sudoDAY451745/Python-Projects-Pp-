name = str(input("\n\n>>> Character printer: <<<\n>Enter a String: "))


def printResult():
    print(f'''
    /---heres the list:---/

> Vowel list:                {resultOfVowels}
> Consonants list:           {resultOfConsonants}
> Special Char list:         {sC}
          ''')


def showNumberOflen():
    print(f'''
    /---heres the special request:---/

> Vowel lenght:               {len(resultOfVowels)}
> Consonants length:          {len(resultOfConsonants)}
> Special Character Lenght:   {len(sC)}

''')


# construction:
uVowels = "AIUEO"
lVowels = uVowels.lower()  # l = lower Vowels

uConsonants = "BCDFGHJKLMNPQRSTVWXYZ"
lConsonants = uConsonants.lower()  # l = lower Consonants

# true consonants and vowels:
consonants = uConsonants + lConsonants
vowels = uVowels + lVowels

# blank Containers:
sC = ""
resultOfVowels = ""
resultOfConsonants = ""

# condition:
for char in name:
    if char == " ":
        continue
    elif char in (vowels):
        resultOfVowels += char

    elif char in (consonants):
        resultOfConsonants += char
    else:
        sC += char

# Results:
while True:
    toggel: str = input(
        ">Would you like to display the length?\n(Yes or No): ").strip().lower()

    if toggel == "yes":
        print("\n\n\n>>> Results are here! <<<")
        printResult()
        showNumberOflen()
        break

    elif toggel == "no":
        print("\n>>> Results are here! <<<")
        printResult()
        break
    else:
        print("request cant be recognized, try again")
