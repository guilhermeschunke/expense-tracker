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

add_expense(expenses)
add_expense(expenses)
add_expense(expenses)

total = calculate_total(expenses)

print("Total expenses:", total)

