str1 = input("Enter A String: ")
result = ""

for char in range(len(str1) - 1, -1, -1):
    result += str1[char]

print(f"\n     >>> Results <<<")
print("=" * 25)
print(f"String:             {str1}")
print(f"Reversed String:    {result}")
print("=" * 25)
