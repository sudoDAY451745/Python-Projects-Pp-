print("\n>>> Tally Counter <<<")
inputString = input("Enter a String: ").lower()

tally = {}

for char in inputString:
    if char == " ":  # filter
        continue

    elif char in tally:
        tally[char] += 1  # Increment if you see it again
    else:
        tally[char] = 1  # if brand new character: add new

print()

# results
for string, value in tally.items():
    print(f"{string} = {value}")

# mali account sir account pala po ng kuya ko po projektday7
