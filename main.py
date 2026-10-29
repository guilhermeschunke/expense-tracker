expenses = []

def add_expense(expenses):
    name = input("Enter the name of the expense: ")
    amount = float(input("Enter the amount of the expense: "))
    expenses.append(amount)


def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense
    return total

while True:
    print("1. Add expense")
    print("2. Calculate total")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_expense(expenses)
    elif choice == '2':
        total = calculate_total(expenses)
        print("Total expenses:", total)
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")


