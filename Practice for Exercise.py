expenses = {}


def summary(expenses, income):
    total = 0
    expense = expenses.values()
    for exp in expense:
        total += exp
    balance = income - total
    if balance > (0.5 * income):
        message = "Great Job! You're saving a lot of money"
    elif balance < (0.5 * income):
        message = "Be careful! You're close to spending all your income."
    elif total > income:
        message = "You're spending too much! Try to cut down on some expenses."
    return total, balance, message


print("Welcome to Budget Buddy App")
while True:
    name = input("Enter your name: ")
    if name:
        print(f"Hi, {name}! Let's Get Started \n\n")
        break

while True:
    try:
        income = float(input("How much do you earn per month?: "))
        break
    except ValueError:
        print("Please enter a number only")

print('Type your expenses and the amount for each. Type "done" when you are finished.  ')
while True:
    current_key = input('Expense: ')
    if current_key == "done":
        total, balance, message = summary(expenses, income)
        print(f"Total Income: P {income:,.2}")
        print(f"Total expenses: P {total:,.2}")
        print(f"Balance: P {balance:,.2}")
        print(message)
        break
    expenses[current_key] = int(input(f"Amount for {current_key}: "))