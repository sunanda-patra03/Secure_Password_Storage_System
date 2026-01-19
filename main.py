from auth import register_user, login_user

def main():
    print("🔐 Secure Password Storage System")

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            success, message = register_user(username, password)
            print(message)

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            success, message = login_user(username, password)
            print(message)

        elif choice == "3":
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
