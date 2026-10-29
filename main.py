expenses = []

expenses.append(65)
expenses.append(100)
expenses.append(50)
expenses.append(200)
expenses.append(30)

total = 0
for expense in expenses:
    total = total + expense
    

print(total)

def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense
    return total

total = calculate_total(expenses)

print("Total expenses:", total)
