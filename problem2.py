# accounts = {
#     "A001": ("Alice", 1000.0),
#     "A002": ("Bob", 500.0)
# }

# def create_account(account_no, name, balance=0):
#     if account_no in accounts:
#         print("Account already exist")
#     else:
#         accounts[account_no] = (name, balance)
#         print("Account added succesfully!")

# def deposit(account_no, amount):
#     try:
#         name, balance = accounts[account_no]
#         if amount <= 0:
#             raise ValueError("Invalid Amount")
#         balance += amount
#         accounts[account_no] = (name, balance)
#         print("Deposit Sucessfully")
#     except KeyError as e:
#         raise KeyError(f'Account {e} not found') from e


# def withdraw(account_no, amount):
#     try:
#         name, balance = accounts[account_no]
#         if amount <= 0:
#             raise ValueError("Invalid Amount")
#         if balance < amount:
#             raise ValueError("Insufficient Fund")
#         balance -= amount
#         accounts[account_no] = (name, balance)
#     except KeyError as e:
#         raise KeyError(f'Account {e} not found') from e
    
# def transfer(from_acc, to_acc, amount):
#     try:
#         fname, fbalance = accounts[from_acc]
#         tname, tbalance = accounts[to_acc]
#         if amount <= 0 :
#             raise ValueError("Invalid Amount")
#         if fbalance < amount:
#             raise ValueError("Insufficient Fund")
#         fbalance -= amount
#         tbalance += amount
#         accounts[from_acc] = (fname, fbalance)
#         accounts[to_acc] = (tname, tbalance)
#     except KeyError as e:
#         raise KeyError(f'Account {e} not found') from e

# def rank_accounts():
#     ranked = sorted(accounts.items(), key=lambda x: x[1][1], reverse=True)
#     for acc_no, (name, balance) in ranked:
#         print(f'Account: {acc_no} | Name: {name} | Balance: {balance}')
    
# transfer("A001", "A004", 200)
# rank_accounts()
            
            
            
products = {
    "Apple": (10.0, 20),
    "Banana": (5.0, 15),
    "Milk": (30.0, 10)
}

cart = {
    
}

def add_to_cart(cart, product, quantity):
    try:
        prod_price, prod_quantity = products[product]
        if quantity <= 0:
            raise ValueError("Invalid Quantity")
        if quantity > prod_quantity:
            raise ValueError("Not enough Stocks")
        prod_quantity -= quantity
        products[product] = (prod_price, prod_quantity)
        cart[product] = cart.get(product, 0) + quantity
    except KeyError as e:
        print(f'Product {e} does not exist')

def remove_from_cart(cart, product, quantity):
    try:
        prod_quantity = cart[product]
        if quantity <= 0:
            raise ValueError("Invalid Quantity")
        if quantity > prod_quantity:
            raise ValueError("Not enough Stocks")
        prod_quantity -= quantity
        if prod_quantity == 0:
            cart.pop(product)
        else:
            cart[product] = prod_quantity
    except KeyError as e:
        print(f'Product {e} does not exist')

def checkout(cart):
    print("Cart:")
    total_price = 0
    for key, value in cart.items():
        price, quantity= products[key]
        print(f'{key} x {value} = {value * price:,.2f}')
        total_price += value * price
    print("-" * 10)
    print(f'Total: {total_price:,.2f}')
    
    
add_to_cart(cart, "Apple", 2)
add_to_cart(cart, "Apple", 2)
remove_from_cart(cart, "Apple", 4)
add_to_cart(cart, "Milk", 1)

checkout(cart)