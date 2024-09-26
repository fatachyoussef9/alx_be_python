def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(shopping_list):
    item = input("item to add: ")
    shopping_list.append(item)
    print(f"'{item}' has been added to the shopping list.")

def remove_item(shopping_list):
    item = input("item to remove: ")
    if item in shopping_list :
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the shopping list.")
    else : print(f"'{item}' was not found in the shopping list.")

def view_list(shopping_list):
    if shopping_list :
        print("\nShopping List:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")
    else : print("The shopping list is currently empty.")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()