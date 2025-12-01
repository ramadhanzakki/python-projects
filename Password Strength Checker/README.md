# Password Strength Checker 🔒

A simple Python-based program to evaluate the strength of user passwords. This program assesses passwords based on several security criteria and provides specific feedback for improvement if the password is considered weak.

This project was created as part of a basic Python programming logic exercise.

## 📋 Features

The program checks the password based on 4 main criteria:

- ✅ **Length:** Ensures the password is longer than 8 characters.
    
- ✅ **Uppercase Letters:** Checks for the presence of capital letters (A-Z).
    
- ✅ **Numbers:** Checks for the presence of digits (0-9).
    
- ✅ **Special Characters:** Checks for unique symbols (such as @, #, $, etc.).
    

### Enhancement

- **Feedback System:** If the password is not perfect, the program provides a list of specific suggestions on what needs to be added (e.g., _"Add a number"_ or _"Add unique characters"_).
    

## 🚀 How to Run the Program

Ensure you have Python installed on your computer.

1. Download or clone this repository.
    
2. Open your terminal or command prompt.
    
3. Run the following command:
    

```
python main.py
```

_(Note: Make sure your Python filename matches, e.g., `password_checker.py`)_

## 📊 Scoring System

The score is calculated based on the number of criteria met (Max Score: 4 or 5).

|Score|Strength Level|
|---|---|
|0 - 1|**Very Weak** 🔴|
|2|**Weak** 🟠|
|3|**Medium** 🟡|
|4|**Strong** 🟢|
|> 4|**Very Strong** 💪|

## 📸 Usage Examples

```
Enter your password : admin
Password strength : Very Weak
Advice for strengthening your password:
- Password is too short
- Add a capital letter
- Add a number
- Add unique characters
```

```
Enter your password : P@ssword123
Password strength : Very Strong
```

## 📚 Reference

This project is based on the guide from **"Python Projects for Beginners"** (Page 17).

_Created with ❤️ for learning Python._