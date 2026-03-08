print("\n>>> String Zipper <<<\n")

# input
Str1 = input("Input Any String: ")
Str2 = input("Input Another String: ")

result = ""

# main Zipper
for a, b in zip(Str1, Str2):
    result += a + b

# excess/stray characters:
if len(Str1) > len(Str2):
    result += Str1[len(Str2):]
else:
    result += Str2[len(Str1):]

print("\n", result)


# mali account sir account pala po ng kuya ko po projektday7
