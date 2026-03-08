result = ""
welcomeMSG = "\n\n>>>  Welcome to Calculator!  <<<\nOptions: "
options = "\n 1 = +\n 2 = -\n 3 = *\n 4 = /\n 5 = exit\n"

operatorOptions = ("1", "2", "3", "4")


def error():
    print("\n You Cant Do That! >:(\nrun again")


print(welcomeMSG)
while (True):
    Operator = str(
        input(f"{options}\nEnter the Operator: ").strip())
    if Operator == "5":
        print("have a nice day! o7")
        break
    elif Operator not in operatorOptions:
        error()
        break

    num1 = int(input("Input your first Number: ").strip())
    if (num1 == 0 and Operator == "4"):
        error()
        break

    num2 = int(input("Input your second Number: ").strip())
    if (num2 == 0 and Operator == "4"):
        error()
        break

    if Operator == "1":
        result = num1 + num2
    elif Operator == "2":
        result = num1 - num2
    elif Operator == "3":
        result = num1 * num2
    elif Operator == "4":
        result = num1 / num2

    message = (f"\n--- your Answer is: {result} ---")

    print(message)
