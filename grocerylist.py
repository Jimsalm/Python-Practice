

print("Grocery List Manager")
print("---------------------")
print("1. Add an item")
print("2. Remove an item")
print("3. View List")
print("4. Quit")

items = []




while True:
    
    input_choice = input("Enter your choice: ")
    input_item = ''
    
    if input_choice == '1':
        input_item = input("Enter the item to add: ")
        items.append(input_item)
        print(f'{input_item} added to the list. \n')

    elif input_choice == '2':
        input_item = input("Enter the item to remove: ");
        if input_item in items:
            items.remove(input_item)
            print(f'{input_item} removed from the list. \n')
        else:
            print(f'No {input_item} in the list\n')
        
    elif input_choice == '3':
        print("Your grocery list:")
        for i in items:
            print(f'- {i}')
        print("\n")
            
    elif input_choice == '4':
        print("Goodbye!")
        break
    
    else:
        print("Choose only between 1 - 4\n")


