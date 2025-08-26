expenses = {}

#Step 1

print("Welcome to Budget Buddy App!")
name = input("Enter your name: ")
print(f'Hi, {name} Let\'s get started\n')

#Step 2

try:
    income = float(input("How much money do you earn per month? "))
except ValueError:
    print("Please enter a number only!")
    exit()
    
#Step 3

print("Type your expenses and the amount for each. Type \"done\" when you are finished.")

while True:
    category = input("Expense: ")
    if category.lower() == 'done':
        break
    else:
        amount = float(input(f'Amount for {category}: '))
        expenses[category] = amount
        
#Step 4
print("\nSummary")
print(f'Total income: P {income:,.2f}')

total_expenses = 0
for amount in expenses.values():
    total_expenses += amount

print(f'Total Expenses: P {total_expenses:,.2f}')

balance = income - total_expenses
print(f'Balance: P {balance:,.2f}')

if income / 2 > total_expenses:
    print("Great Job! You\'re saving a lot of money.")
elif income < total_expenses:
    print("You're Spending too much! Try to cut down on some expenses")
else:
    print("Be Careful! You're close to spending all your income.")
    
#Step 5

print("\nReport:")
highest_value = 0
highest_key = ''
for key, value in expenses.items():
    print(f'{key}: P {value:,.2f} = {(value/income) * 100:,.2f}%')
    if value > highest_value:
        highest_value = value
        highest_key = key

print(f'The highest expense is {highest_key} for P {expenses[highest_key]:,.2f}.')