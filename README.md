# Online Banking Program

This is a simple online banking program that allows users to perform various banking operations. Below are the functionalities provided by the program:

1. **Login:** Users can log in to their accounts by providing a valid username and password.

2. **Signup:** New users can create an account by providing a unique username and a valid password.

3. **Change Password:** Users can change their account password after logging in by providing the old and new passwords.

4. **Delete Account:** Users can delete their accounts after logging in by providing the account username and password.

5. **Update Amount:** Users can update their account balance by depositing or withdrawing money.

6. **Make a Transfer:** Users can transfer money between accounts.

7. **Exit:** Users can exit the program.

## Functions

1. **`valid_password(password)`**
   - Validates the given password based on certain criteria (length, uppercase, lowercase, digit).
   - Returns `True` if the password is valid; otherwise, returns `False`.

2. **`import_and_create_bank(filename)`**
   - Imports and creates a bank dictionary from a given file containing transactions.
   - Returns the bank dictionary.

3. **`import_and_create_accounts(filename)`**
   - Imports and creates user accounts from a given file.
   - Returns dictionaries of user accounts and login status.

4. **`signup(user_accounts, log_in, username, password)`**
   - Allows users to sign up, checking and validating the provided username and password.
   - Returns `True` if the signup is successful; otherwise, returns `False`.

5. **`login(user_accounts, log_in, username, password)`**
   - Allows users to log in by verifying the provided username and password.
   - Returns `True` if the login is successful; otherwise, returns `False`.

6. **`update(bank, log_in, username, amount)`**
   - Updates the user's bank balance based on the provided amount.
   - Returns `True` if the update is successful; otherwise, returns `False`.

7. **`transfer(bank, log_in, userA, userB, amount)`**
   - Transfers money from one user to another.
   - Returns `True` if the transfer is successful; otherwise, returns `False`.

8. **`change_password(user_accounts, log_in, username, old_password, new_password)`**
   - Changes the user's password after verifying the old password and validating the new one.
   - Returns `True` if the password change is successful; otherwise, returns `False`.

9. **`delete_account(user_accounts, log_in, bank, username, password)`**
   - Deletes a user account after verifying the username and password.
   - Returns `True` if the account deletion is successful; otherwise, returns `False`.

10. **`main()`**
    - The main function where users can interact with the program. It provides a menu to choose different options.

## How to Run

1. Ensure that you have the necessary input files (`bank.txt` and `user.txt`) in the correct format.

2. Run the program and follow the on-screen instructions to perform banking operations.

3. Choose options from the menu to log in, sign up, change password, delete account, update amount, make a transfer, or exit.

4. The program provides feedback on the success or failure of each operation.

Feel free to explore the code, and enjoy using this simple online banking program!
