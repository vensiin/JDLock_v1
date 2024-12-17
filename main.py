from JDLock_classes import *
import tkinter
from tkinter import ttk
from tkinter import Entry
from tkinter import messagebox
import json


# Blank frame with 2 buttons
class Main_Window_frame():
    def __init__(self, master):
        # Main Frame that holds all the menu shit on the main window ("master")
        main_frame = tkinter.Frame(master, bg="#317ba3")
        main_frame.pack()

        self.frameIndex = 1  # Initialized to one to forget: options_frame
        self.frameList = [main_menu(main_frame), options_frame(main_frame)]  # List of all the current frames we have
        self.frameList[self.frameIndex].forget()  # Forgets current index frame (options_frame)
        self.frameList[0].pack()  # Packs the 0 index frame main_menu, so it is the first frame that is shown

        # Frame that holds all the button/actions at the bottom
        bottom_frame = tkinter.Frame(master, bg="#317ba3")
        bottom_frame.pack()

        # Menu button that opens new window (for now)
        self.view_menu_button = tkinter.Button(bottom_frame,
                                               text="View Menu",
                                               font=('fantasy', 10, 'bold'),
                                               height=3,
                                               width=20,
                                               padx=100,
                                               pady=1,
                                               bg="gray",
                                               fg="yellow",
                                               relief="ridge",
                                               bd=10,
                                               cursor="hand2",
                                               command=self.changeWindow
                                               )
        self.view_menu_button.pack(pady=50)

        self.main_exit_button = tkinter.Button(bottom_frame,
                                               text="Exit JDLock",
                                               font=('fantasy', 10, 'bold'),
                                               height=3,
                                               width=20,
                                               padx=100,
                                               pady=1,
                                               bg="gray",
                                               fg="yellow",
                                               relief="ridge",
                                               bd=10,
                                               cursor="hand2",
                                               command=master.quit
                                               )
        self.main_exit_button.pack(pady=5)

    # Change window function used to change the frame
    def changeWindow(self):
        self.frameList[self.frameIndex].forget()  # Forgets current frame
        self.frameIndex = (self.frameIndex + 1) % len(self.frameList)  # Cycles through the frames
        self.frameList[self.frameIndex].tkraise()  # Raises the current frame/frameIndex to user view
        self.frameList[self.frameIndex].pack()  # Repacks frame

        if self.frameIndex == 1:
            self.view_menu_button.forget()
            self.main_exit_button.forget()


# First window
class main_menu(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # Image icon
        self.JDLock_icon = tkinter.PhotoImage(file="170x245_logo.png")

        # Front page label
        frontpage_label = tkinter.Label(self,
                                        text="JDLock",
                                        font=('fantasy', 100, 'bold'),
                                        fg="yellow",
                                        bg="gray",
                                        relief="ridge",
                                        bd=50,
                                        padx=50,
                                        pady=50,
                                        image=self.JDLock_icon,
                                        compound="right"
                                        )
        frontpage_label.pack()


# Second window
class options_frame(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.jdlock = UserPassword()
        options_menu = tkinter.Frame(self, bg="#317ba3")
        options_menu.pack()

        # Label that greets/prompts
        greet_User = tkinter.Label(options_menu,
                                   text="How can we help you today?",
                                   font=('fantasy', 40, 'bold'),
                                   fg="yellow",
                                   bg="gray",
                                   relief="ridge",
                                   bd=10,
                                   padx=100,
                                   pady=10
                                   )
        greet_User.pack()

        # Frame that holds all the buttons/actions
        menu_frame = tkinter.Frame(options_menu, bg="#317ba3",
                                   relief="sunken",
                                   bd=100,
                                   borderwidth=0,
                                   highlightthickness=0)
        menu_frame.pack(pady=50, padx=0)

        # View passwords button to view your password(s)
        view_passwords_button = tkinter.Button(menu_frame,
                                               text="View Passwords",
                                               font=('fantasy', 12, 'bold'),
                                               bg="gray",
                                               fg="yellow",
                                               width=20,
                                               cursor="hand2",
                                               command=self.display_passwords
                                               )
        view_passwords_button.pack(side="left", padx=20)

        # Add password button to add password(s)
        add_password_button = tkinter.Button(menu_frame,
                                             text="Add Password",
                                             font=('fantasy', 12, 'bold'),
                                             fg="yellow",
                                             bg="gray",
                                             cursor="hand2",
                                             command=self.display_add_password
                                             )
        add_password_button.pack(side="left", padx=20)

        # Change password button to change password(s)
        change_password_button = tkinter.Button(menu_frame,
                                                text="Change Password",
                                                font=('fantasy', 12, 'bold'),
                                                fg="yellow",
                                                bg="gray",
                                                cursor="hand2",
                                                command=self.change_password
                                                )
        change_password_button.pack(side="left", padx=20)

        # Delete password button to delete password(s)
        delete_password_button = tkinter.Button(menu_frame,
                                                text="Delete Password",
                                                font=('fantasy', 12, 'bold'),
                                                fg="yellow",
                                                bg="gray",
                                                cursor="hand2",
                                                command=self.display_delete_password
                                                )
        delete_password_button.pack(side="left", padx=20)

        # Create a new frame for the specified button clicked
        self.content_frame = tkinter.Frame(options_menu, bg="#317ba3")
        self.content_frame.pack()

    # Clears the widgets in a frame
    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    # Displays a listbox of all the account name and passwords
    def display_passwords(self):
        self.clear_content()  # Clears the current widgets in the frame
        user_passwords = self.jdlock.fetch_passwords()  # Fetch passwords and the account associated with the password

        # Initialized ListBox that holds the account and the account password
        self.password_listbox = tkinter.Listbox(self.content_frame,
                                                font=('fantasy', 12, 'bold'),
                                                bg="gray",
                                                fg="yellow",
                                                width=50,
                                                height=10)
        self.password_listbox.pack()

        # Populate the listbox with account names and passwords
        for Account, Account_Passwords in user_passwords:
            self.password_listbox.insert(tkinter.END, f"{Account}: {Account_Passwords}")

    # Displays entire add_password function
    def display_add_password(self):
        self.clear_content()

        # Account Section
        self.account_frame = tkinter.Frame(self.content_frame, bg="#317ba3")

        # Label for account name
        accountname_label = tkinter.Label(self.account_frame,
                                          text="Account Name: ",
                                          font=('fantasy', 13, 'bold'),
                                          fg="yellow",
                                          bg="gray",
                                          width=13,
                                          relief="flat",
                                          bd=4)
        accountname_label.pack(side=tkinter.LEFT, pady=10)

        # Entry box to put in account name
        self.accountEntry = tkinter.Entry(self.account_frame,
                                          font=('fantasy', 13, 'bold'),
                                          fg="yellow", bg="gray",
                                          width=50, relief="flat",
                                          bd=4)
        self.accountEntry.pack(side=tkinter.RIGHT)
        self.accountEntry.focus()

        # Packed after everything to remain order because the order of the pack DOES matter
        self.account_frame.pack()

        # Password section
        self.password_frame = tkinter.Frame(self.content_frame,
                                            bg="#317ba3")
        self.password_frame.pack()

        # Password frame that holds the password label/entry
        password_label = tkinter.Label(self.password_frame,
                                       text="Password : ",
                                       font=('fantasy', 13, 'bold'),
                                       fg="yellow",
                                       bg="gray",
                                       width=13,
                                       relief="flat",
                                       bd=4)
        password_label.pack(side=tkinter.LEFT, pady=10)

        # Entry box to put in password for account name
        self.passwordEntry = tkinter.Entry(self.password_frame,
                                           font=('fantasy', 13, 'bold'),
                                           fg="yellow",
                                           bg="gray",
                                           width=50,
                                           relief="flat",
                                           bd=4)
        self.passwordEntry.pack(side=tkinter.RIGHT)

        # Submit button
        submit_button = tkinter.Button(self.content_frame,
                                       text="Submit",
                                       font=('fantasy', 13, 'bold'),
                                       fg="yellow",
                                       bg="navajowhite3",
                                       activebackground="cadet blue",
                                       cursor="hand2",
                                       relief="raised",
                                       bd=4,
                                       command=self.submit_addPassword)
        submit_button.pack(side=tkinter.BOTTOM, pady=10)

    # Calls the add_password_entry function in the JDLock_classes file
    def submit_addPassword(self):
        # Variable that is holding account name
        accountName = self.accountEntry.get()

        # Variable holding Account password
        passwordName = self.passwordEntry.get()

        # Function that calls the add_password_entry function in the JDlock classes file with parameters so it has access
        add_new = self.jdlock.add_password_entry(accountName, passwordName)
        messagebox.showinfo("Awesome", "Password saved successfully!")

    # submits delete request
    def submit_deletePassword(self):

        selected_accounts = self.password_listbox.curselection()  # Select item(s) from the box
        if selected_accounts:  # Check if there is a selection
            for index in selected_accounts:  # Iterates through all the account(s) the user selected

                # Get only the account name because the listbox in this function only displays the account names
                account = self.password_listbox.get(index).split(":")[0]

                delete_success = self.jdlock.delete_password(account)  # Call delete password function in the JDlock_classes

        messagebox.showinfo("Success", f"Password for {account} deleted successfully!")

        self.display_delete_password()  # refresh the list of accounts

    # Displays the delete password frame
    def display_delete_password(self):
        self.clear_content()
        user_passwords = self.jdlock.fetch_passwords() # Variable that holds passwords

        # Create a listbox to display accounts
        self.password_listbox = tkinter.Listbox(self.content_frame,
                                                font=('fantasy', 12, 'bold'),
                                                bg="gray",
                                                fg="yellow",
                                                width=50,
                                                height=10,
                                                selectmode="multiple")
        self.password_listbox.pack()

        # Populate the listbox with only the account names, the _ ignores the passwords since we are iterating through a tuple
        for account, _ in user_passwords:
            self.password_listbox.insert(tkinter.END, account)

        # Submit button
        submit_button = tkinter.Button(self.content_frame,
                                       text="Delete Selected",
                                       font=('fantasy', 13, 'bold'),
                                       fg="yellow",
                                       bg="navajowhite3",
                                       activebackground="cadet blue",
                                       cursor="hand2",
                                       relief="raised",
                                       bd=4,
                                       command=self.submit_deletePassword)
        submit_button.pack(side=tkinter.BOTTOM, pady=10)

    # This submits the changed password
    def submit_changedPassword(self):

        # This selects the account on the listbox
        selected_account = self.password_listbox.curselection()

        if selected_account:
            # Get only the account name because the listbox in this function only displays the account names
            account = self.password_listbox.get(selected_account).split(":")[0]

            New_Password = self.ChangePW_Entry.get() # This is the new password the user is inputting

            # Calls the change_password function in the JDLock_classes file with the account and new_password as parameters
            change_success = self.jdlock.change_password(account,New_Password)

        messagebox.showinfo("Success", f"Password has changed successfully!")

        self.display_passwords() # Displays passwords after the button is clicked

    # Displays the change password frame
    def change_password(self):
        self.clear_content()
        user_passwords = self.jdlock.fetch_passwords()

        # Change PW frame because we needed 2 seperate frames so the change password button wouldn't be within the listbox/entrybox
        self.changePW_frame = tkinter.Frame(self.content_frame, bg="#317ba3")

        #Create a listbox to display accounts
        self.password_listbox = tkinter.Listbox(self.changePW_frame,
                                                font=('fantasy', 12, 'bold'),
                                                bg="gray",
                                                fg="yellow",
                                                width=50,
                                                height=10,
                                                selectmode="single")
        self.password_listbox.pack()

        # Populate the listbox with only the account names, the _ ignores the passwords since we are iterating through a tuple
        for account, _ in user_passwords:
            self.password_listbox.insert(tkinter.END, account)

        # Label for the ChangePW entry box
        ChangePW_label = tkinter.Label(self.changePW_frame,
                                          text="New Password : ",
                                          font=('fantasy', 13, 'bold'),
                                          fg="yellow",
                                          bg="gray",
                                          width=13,
                                          relief="flat",
                                          bd=4)
        ChangePW_label.pack(side=tkinter.LEFT, pady=10)

        self.ChangePW_Entry = tkinter.Entry(self.changePW_frame,
                                          font=('fantasy', 13, 'bold'),
                                          fg="yellow", bg="gray",
                                          width=35, relief="flat",
                                          bd=4)
        self.ChangePW_Entry.pack(side=tkinter.RIGHT)
        self.ChangePW_Entry.focus()


        # Packed after everything to remain order because the order of the pack DOES matter
        self.changePW_frame.pack()


        # Submit button
        submit_button = tkinter.Button(self.content_frame,
                                       text="Change Password for this account",
                                       font=('fantasy', 13, 'bold'),
                                       fg="yellow",
                                       bg="navajowhite3",
                                       activebackground="cadet blue",
                                       cursor="hand2",
                                       relief="raised",
                                       bd=4,
                                       command=self.submit_changedPassword)
        submit_button.pack(side=tkinter.BOTTOM, pady=10)





def main_window_open():
    root = tkinter.Tk(screenName="JDLock", baseName="JDLock", className="TK")
    root.title("JDLock")
    root.configure(background="#317ba3")

    startup_window = Main_Window_frame(root)

    root.mainloop()


main_window_open()
