# Generate-Strong-Password-
This Python script provides a simple graphical user interface (GUI) for generating random passwords with various character types.
 It utilizes the tkinter library for the GUI components and offers the following functionality:

Features:
Generate Password: The core functionality of the application is the generation of random passwords. Users can specify the number of characters they want in the generated password.

Character Composition: The generated password is designed to have a specific character composition:

30% lowercase letters
30% uppercase letters
20% digits
20% punctuation symbols
Validation: The application performs input validation to ensure the entered character count is a valid number and is greater than or equal to 6 characters. It displays appropriate error messages if the input is invalid.

Components:
Entry Fields: There are two entry fields in the GUI:

"Number of Characters": Users input the desired length of the password here.
"Generated Password": The generated password is displayed in this field.
Generate Password Button: Clicking this button triggers the password generation process.

Labels: The GUI contains labels to provide instructions and display the generated password.

Usage:
Enter the desired number of characters for your password in the "Number of Characters" entry field.

Click the "Generate Password" button to generate a random password.

The generated password will be displayed in the "Generated Password" entry field.

If the input is invalid (less than 6 characters or not a valid number), error messages will be shown.

Dependencies:
The code uses the string and random modules from Python's standard library for character generation and shuffling.
The tkinter library is used for creating the graphical user interface.
Notes:
The code assumes Python 3 and tkinter are installed on the system.
Feel free to use, modify, or share this password generator application as needed. If you encounter any issues or have suggestions for improvements, please feel free to contribute to the GitHub repository.
