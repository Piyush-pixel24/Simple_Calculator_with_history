History_File = "history.txt"

# 🔹 Show History
def show_History():
    try:
        file = open(History_File, 'r')
        lines = file.readlines()

        if len(lines) == 0:
            print("History not found")
        else:
            print("\n--- Calculation History ---")
            for line in reversed(lines):
                print(line.strip())

        file.close()

    except FileNotFoundError:
        print("No history file found")


# 🔹 Clear History
def clear_History():
    file = open(History_File, 'w')
    file.close()
    print("History cleared !!!")


# 🔹 Save History
def save_History(equation, result):
    file = open(History_File, 'a')
    file.write(equation + " = " + str(result) + "\n")
    file.close()


# 🔹 Calculator Logic 
def calculate(user_input):
    parts = user_input.split()

    if len(parts) != 3:
        print("Invalid input... Use format: 4 + 4")
        return

    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Invalid numbers entered")
        return

    # Operations - add , subract , multiply , divide .
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == 'x' or op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print("Cannot divide by zero")
            return
        result = num1 / num2
    else:
        print("Invalid operator")
        return

    # Remove .0 if it is integer
    if int(result) == result:
        result = int(result)

    print(f"RESULT: {result}")

    # Save history
    save_History(user_input, result)


# 🔹 Main Function
def main():
    print("WELCOME TO SIMPLE CALCULATOR")

    while True:
        user_input = input("\nEnter calculation (+, -, x, /) or 'history' or 'clear' or 'exit': ")

        if user_input.lower() == "exit":
            print("EXITED...")
            break
        elif user_input.lower() == "history":
            show_History()
        elif user_input.lower() == "clear":
            clear_History()
        else:
            calculate(user_input)


# 🔹 Run Program
main()


    
