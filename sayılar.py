users = {
    "carl": {"password": "1515", "balance": 1000},
    "rei": {"password": "2525", "balance": 500}
}
def login():
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username]["password"] == password:
        print("Login successful")
        return username
    else:
        print("Invalid login")
        return None
def atm(username):
    while True:
        print("\n1- Check Balance")
        print("2- Deposit Money")
        print("3- Withdraw Money")
        print("4- Exit")

        choice = input("Select an option: ")

        if choice == "1":
            print("Balance:", users[username]["balance"])

        elif choice == "2":
            amount = int(input("Enter deposit amount: "))
            users[username]["balance"] += amount
            print("New balance:", users[username]["balance"])

        elif choice == "3":
            amount = int(input("Enter withdrawal amount: "))
            if users[username]["balance"] >= amount:
                users[username]["balance"] -= amount
                print("New balance:", users[username]["balance"])
            else:
                print("Insufficient balance")

        elif choice == "4":
            print("Logged out")
            break

        else:
            print("Invalid option")

user = login()

if user:
    atm(user)