#ex 3 devami

import auth
def main():
    while True:
        print("\nUser Authentication System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option:")

        if choice == "1":
            username = input("Enter username:")
            password = input("Enter password:")
            auth.register(username, password)
        elif choice == "2":
            username = input("Enter username:")
            password = input("Enter password:")
            auth.login(username, password)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

