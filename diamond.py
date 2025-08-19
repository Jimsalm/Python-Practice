

user_input = int(input("Enter size of the Diamond: "))
diamond = ''

for i in range(1, user_input + 1):
    print(" " * (user_input - i), end="")
    print("*" * (2 * i - 1))

for i in range(user_input - 1, 0, -1):
    print(" " * (user_input - i), end="")
    print("*" * (2 * i - 1 ))