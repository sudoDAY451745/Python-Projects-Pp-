name = str(input(
    "\n\n>>> Vowels, Consonants, and Special Character printer: <<<\nEnter a String: "))

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
print("\nVowels only:", resultOfVowels)
print("Consonants only:", resultOfConsonants)
print("Special Characters only:", sC)  # sC = Special Characters

# mali account sir account pala po ng kuya ko po projektday7
