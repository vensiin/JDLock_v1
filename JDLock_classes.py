import os
import json


class UserPassword:

    def __init__(self):
        self._my_passwords = []

    def menu(self):
        print("Welcome to JDLock!")
        print("How can we help you?")
        options = input(
            "1.View Passwords\n2.Add Password\n3.Change Password\n4.Delete Password\n5.Exit\nSelect an option (1-5):")
        os.system('cls')

        while options != "5":
            if options == "1":
                self.get_passwords()
            elif options == "2":
                self.add_password()
            elif options == "3":
                self.change_password()
            elif options == "4":
                self.delete_password()
            elif options == "5":
                print("Thank you for using JDLock")
            else:
                print("That is not a valid option")
            options = input(
                "1.View Passwords\n2.Add Password\n3.Change Password\n4.Delete Password\n5.Exit\nSelect an option (1-5):")
            os.system('cls')
        # print("Hey")

    def get_passwords(self):
        # Opens JSON File to READ as json_file
        with open("passwords.json", "r") as json_file:
            # Initializes password_data as the JSON File to read through
            password_data = json.load(json_file)
            # Iterates through the Decrypted_Passwords and goes through the "Account_Password"
            for passwords in password_data["Decrypted_Passwords"]:
                # print(passwords["Account"])
                print(passwords["Account"] + ": " + passwords["Account_Password"])

    def fetch_passwords(self):
        with open("passwords.json", "r") as json_file:
            password_data = json.load(json_file)
            pwd = [(passwords["Account"], passwords["Account_Password"]) for passwords in
                   password_data["Decrypted_Passwords"]]
            return pwd

    def get_accounts(self):
        # Opens JSON File to READ as json_file
        with open("passwords.json", "r") as json_file:
            # Initializes account_data as the JSON File
            account_data = json.load(json_file)
            # Iterates through the "Account" in the Decrypted_Passwords
            for accounts in account_data["Decrypted_Passwords"]:
                print(accounts["Account"])

    def add_password(self):
        try:
            # Opens JSON File to READ as json_file
            with open("passwords.json", "r") as json_file:
                # Initializes account_data as the JSON File
                password_data = json.load(json_file)

            # Initializes a variable named current_index that holds the length of password_data
            current_index = len(password_data["Decrypted_Passwords"])

            # Prompts users to input how many passwords they would like to add
            num_passwords = int(input("How many passwords would you like to add? (Press 0 to quit): \n"))

            # Loops n number of times (However many passwords the user wants to put)
            for i in range(num_passwords):
                # Prints i
                # print(i)

                # Prints the current index of the passwords in the JSON File
                # Ex. If there are 3 passwords in the JSON File, the current index would start at 4 until the password is inputted
                print(current_index)

                # Asks the user to input the Account name for the password at the current index
                Account = input(f"Enter Account name for password {current_index + i + 1}:")
                # Asks the user to input the Account Password for the Account at the current index
                new_password = input(f"Enter your Password for {Account}: ")

                # Initialize a variable called passwords which holds the Account name and the Account Password in a certain format
                passwords = {
                    "Account": Account,
                    "Account_Password": new_password
                }
                # Appends the passwords variable to the JSON_File
                password_data["Decrypted_Passwords"].append(passwords)

            # Dumps the password_data into the JSON.file
            with open("passwords.json", "w") as json_file:
                json.dump(password_data, json_file, indent=2)

            print("Completed!")

        except FileNotFoundError:
            print("Error: passwords.json file not found.")

    def add_password_entry(self, account_name, new_password):
        try:
            # Read existing passwords from the JSON file
            with open("passwords.json", "r") as json_file:
                password_data = json.load(json_file)

            # Add the new account and password
            passwords = {
                "Account": account_name,
                "Account_Password": new_password
            }
            password_data["Decrypted_Passwords"].append(passwords)

            # Write updated passwords back to the file
            with open("passwords.json", "w") as json_file:
                json.dump(password_data, json_file, indent=2)

            print(f"Password for {account_name} added successfully!")

        except FileNotFoundError:
            print("Error: passwords.json file not found.")

    def change_password(self):
        # Outputs all the users' passwords
        self.get_passwords()

        # Opens JSON File to READ as json_file
        with open("passwords.json", "r") as json_file:
            # Initializes account_data as the JSON File
            password_data = json.load(json_file)

        # Prompts users to input which password they would like to change
        user_change = input("Which password would you like to change? (Enter password exactly as is): ")

        # Prompts users to input what they would like to change it to
        new_password = input("Enter the new password: ")

        # Iterates through the Decrypted_Passwords JSON
        for Account_Password in password_data["Decrypted_Passwords"]:
            # Conditional that checks if the input that the user put is in the JSON File
            if user_change == Account_Password["Account_Password"]:
                Account_Password["Account_Password"] = new_password
                print(f"The Password {user_change} Has Been successfully Changed to: {new_password}!")
            else:
                pass
        with open("passwords.json", "w") as json_file:
            json.dump(password_data, json_file, indent=2)

    def change_account(self):
        self.get_passwords()
        with open("passwords.json", "r") as json_file:
            account_data = json.load(json_file)

        user_change = input("Which Account would you like to change? (Enter account exactly as is): ")
        new_password = input("Enter the new account name: ")

        for Account in account_data["Decrypted_Passwords"]:
            if user_change == Account["Account"]:
                Account["Account"] = new_password
                print(f"The Account name {user_change} Has Been successfully Changed to: {new_password}!")
            else:
                pass
        with open("passwords.json", "w") as json_file:
            json.dump(account_data, json_file, indent=2)

    # Modify the delete_password method in UserPassword class
    def delete_password(self, account_name):
        with open("passwords.json", "r") as json_file:
            password_data = json.load(json_file)

        # Find the account and password to delete
        for account_info in password_data["Decrypted_Passwords"]:
            if account_info["Account"] == account_name:
                password_data["Decrypted_Passwords"].remove(account_info)
                print(f"The account {account_name} and its password have been successfully deleted!")

        # Write updated data back to the JSON file
        with open("passwords.json", "w") as json_file:
            json.dump(password_data, json_file, indent=2)


# Prompt terminal
'''
def main():
    userAccount = UserPassword()
    userAccount.menu()


main()
'''
