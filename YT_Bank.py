import os
FILENAME = "bank_accounts.txt"
# Create file if not exists
if not os.path.exists(FILENAME):
    open(FILENAME, mode="w").close()


def create_account():
    print("\n--- Creating New Account ---")
    acc_no = input("Enter Account Number: ")
    name = input("Enter Account Holder Name: ")
    acc_type = input("Enter Account Type (Saving/Current): ")
    password = input("Set a Password (for withdrawals): ")
    balance = float(input("Enter Initial Amount (>= 500): "))

    if balance < 500:
        print("Minimum balance must be 500!")
        return

    with open(FILENAME, "a") as f:
        f.write(f"{acc_no},{name},{acc_type},{balance},{password}\n")

    print("✅ Account created successfully.")



def deposit_amount():
    print("\n--- Deposit Amount ---")
    acc_no = input("Enter Account Number: ")
    amount = float(input("Enter Amount to Deposit: "))
    updated = False
    lines = []

    with open(FILENAME, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if parts[0] == acc_no:
                parts[3] = str(float(parts[3]) + amount)
                updated = True
            lines.append(",".join(parts))

    if updated:
        with open(FILENAME, "w") as f:
            f.write("\n".join(lines) + "\n")
        print("Amount deposited successfully.")
    else:
        print("Account not found.")


def withdraw_amount():
    print("\n--- Withdraw Amount ---")
    acc_no = input("Enter Account Number: ")
    password = input("Enter Password: ")
    amount = float(input("Enter Amount to Withdraw: "))
    updated = False
    lines = []

    with open(FILENAME, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if parts[0] == acc_no:
                if parts[4].strip() != password.strip():
                    print(" Incorrect password.")
                    return
                current_balance = float(parts[3])
                if current_balance >= amount:
                    parts[3] = str(current_balance - amount)
                    updated = True
                else:
                    print(" Insufficient balance.")
                    return
            lines.append(",".join(parts))

    if updated:
        with open(FILENAME, "w") as f:
            f.write("\n".join(lines) + "\n")
        print(" Amount withdrawn successfully.")
    else:
        print(" Account not found.")



def balance_enquiry():
    print("\n--- Balance Enquiry ---")
    acc_no = input("Enter Account Number: ")
    with open(FILENAME, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if parts[0] == acc_no:
                print(f" Account No: {parts[0]},  Balance: ₹{parts[3]}")
                return
    print(" Account not found.")




def display_all_accounts():
    print("\n--- All Account Holders ---")
    with open(FILENAME, "r") as f:
        for line in f:
            acc_no, name, acc_type, balance, _ = line.strip().split(",")
            print(f"Account No: {acc_no}, Name: {name}, Type: {acc_type}, Balance: ₹{balance}")



def close_account():
    print("\n--- Close Account ---")
    acc_no = input("Enter Account Number to Close: ")
    found = False
    lines = []

    with open(FILENAME, "r") as f:
        for line in f:
            if not line.strip().startswith(acc_no + ","):
                lines.append(line.strip())
            else:
                found = True

    if found:
        with open(FILENAME, "w") as f:
            f.write("\n".join(lines) + "\n")
        print(" Account closed successfully.")
    else:
        print(" Account not found.")




def modify_account():
    print("\n--- Modify Account ---")
    acc_no = input("Enter Account Number to Modify: ")
    updated = False
    lines = []

    with open(FILENAME, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if parts[0] == acc_no:
                name = input("Enter New Name: ")
                acc_type = input("Enter New Account Type: ")
                parts[1] = name
                parts[2] = acc_type
                updated = True
            lines.append(",".join(parts))

    if updated:
        with open(FILENAME, "w") as f:
            f.write("\n".join(lines) + "\n")
        print(" Account modified successfully.")
    else:
        print(" Account not found.")




while True:
    print("\n<<< BANK MANAGEMENT SYSTEM >>>")
    print("1. Open New Account")
    print("2. Deposit Amount")
    print("3. Withdraw Amount (Password Protected)")
    print("4. Balance Enquiry")
    print("5. All Account Holder List")
    print("6. Close Account")
    print("7. Modify Account")
    print("8. Exit")

    choice = input("Enter Your Choice (1-8): ")

    if choice == '1':
        create_account()
    elif choice == '2':
        deposit_amount()
    elif choice == '3':
        withdraw_amount()
    elif choice == '4':
        balance_enquiry()
    elif choice == '5':
        display_all_accounts()
    elif choice == '6':
        close_account()
    elif choice == '7':
        modify_account()
    elif choice == '8':
        print("!!! Thank you for using the Bank Management System.")
        break
    else:
        print("Invalid choice. Please try again.")
