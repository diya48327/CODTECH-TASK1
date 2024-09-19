# CODTECH-TASK1
Name:Diya Saha
Company:CODTECT IT SOLUTIONS
ID:CT12DS1931
Domain:Cyber Security & Ethical Hacking
Duration:JULY to SEPTEMBER 2024
Mentor:Muzammil Ahmed

Project Documentation for Password Strength Assessment Tool
1. Project Overview
Project Name: Password Strength Assessment Tool
Description:
The Password Strength Assessment Tool is a Python-based program that evaluates the strength of user-entered passwords based on length, complexity, and uniqueness. The tool provides feedback on how to improve the password to meet security standards by analyzing factors such as uppercase letters, lowercase letters, numbers, special characters, and avoidance of common patterns. This project ensures that users create strong and secure passwords by delivering real-time feedback.

2. Objectives
Evaluate password strength based on length, complexity, and uniqueness.
Provide feedback to help users improve weak or moderate passwords.
Enhance security by guiding users to avoid commonly used and predictable patterns.
Classify passwords into categories such as "Strong", "Moderate", or "Weak".
3. Features
Length Analysis: Ensures the password is long enough for better security.
Complexity Analysis: Evaluates the presence of uppercase letters, lowercase letters, numbers, and special characters.
Common Patterns Check: Detects and discourages the use of predictable patterns like "123456", "password", etc.
Real-Time Feedback: Provides suggestions on how to improve password strength.
Score-Based Classification: The tool classifies the password as Strong, Moderate, or Weak based on the total score.
4. Functional Requirements
Input:
The tool accepts a user-provided password as input.
Output:
Strength Classification: Outputs the password's strength as "Weak", "Moderate", or "Strong".
Feedback: Provides a list of suggestions for improving the password, such as adding uppercase letters, digits, special characters, etc.
5. Non-Functional Requirements
Usability: The tool should be easy to use, providing immediate feedback after a password is entered.
Portability: The tool can run on any system that supports Python.
Maintainability: The code is modular and easy to modify for additional features or complexity checks.
Security: The tool should not store or log any user passwords.
6. Technical Specifications
Technology Stack:
Programming Language: Python 3.8 or above
Library: re (Regular Expressions) for pattern matching
System Requirements:
Python Installation: Python 3.x installed on the system.
Operating System: Cross-platform (Windows, macOS, Linux).
7. Implementation Details
Algorithm Logic:
Length Check:

If the password length is 12 characters or more, it gets 2 points.
If the password is between 8 and 12 characters, it gets 1 point.
If the password is less than 8 characters, feedback is provided to make the password longer.
Uppercase, Lowercase, Digits, and Special Characters:

Each of these categories adds 1 point to the password’s score if present.
If any of these elements are missing, feedback suggests adding them.
Common Patterns Check:

The password is checked against a list of common patterns (e.g., "123456", "password", etc.). If found, feedback suggests avoiding these patterns. If not found, the password is rewarded with 1 additional point.
Scoring System:

A total score is calculated, and based on the score, the password is classified as:
Strong: If the score is 7 or above.
Moderate: If the score is between 4 and 6.
Weak: If the score is less than 4.
8. Code Documentation
assess_password_strength(password)
Input: A string representing the password.
Output: Returns the password strength (Weak, Moderate, Strong) and a list of feedback suggestions for improvement.
Purpose: This function evaluates the password based on length, character variety, and uniqueness, providing both a strength classification and improvement tips.
main()
Purpose: Serves as the entry point for the program. It prompts the user to enter a password, calls the assess_password_strength() function, and displays the results and feedback.
9. Testing and Validation
Test Cases:
Test Case 1:
Input: "Password123!"
Expected Output:
Password Strength: Moderate
Feedback:

Add at least one special character (e.g., !, @, #, $, etc.).
Test Case 2:
Input: "abcd1234"
Expected Output:
Password Strength: Weak
Feedback:

Add at least one uppercase letter (A-Z).
Add at least one special character (e.g., !, @, #, $, etc.).
Password is too short. Consider making it at least 12 characters.
Test Case 3:
Input: "Pa$$w0rd!!2024"
Expected Output:
Password Strength: Strong
Feedback:

None.
Testing Strategy:
Perform unit testing for individual functions (e.g., length checks, pattern checks).
Conduct end-to-end testing by simulating user input and verifying the output feedback and classification.
10. Deployment
Steps:
Install Python: Ensure that Python 3.x is installed on the machine.
Run the Program:
Open the terminal or command prompt.
Navigate to the project folder.
Run the script using the command:
bash
Copy code
python password_strength_tool.py
User Input: The program will prompt the user to enter a password and then display the strength and feedback.
11. Future Enhancements
Entropy Calculation: Implement more advanced metrics to calculate the entropy of the password and ensure randomness.
Blacklist Integration: Cross-check passwords against a larger, regularly updated blacklist of compromised or weak passwords.
GUI Version: Develop a graphical user interface (GUI) to make the tool more user-friendly.
Multilingual Support: Offer feedback in multiple languages to cater to a broader audience.
12. Conclusion
The Password Strength Assessment Tool is an efficient utility that helps users create stronger, more secure passwords by providing immediate feedback. By checking various aspects of the password's complexity and uniqueness, the tool promotes best practices in password creation, ultimately enhancing overall security for users.
