import re

# Function to assess password strength
def assess_password_strength(password):
    # Initialize scores and feedback variables
    score = 0
    feedback = []

    # Check for length
    if len(password) >= 12:
        score += 2
        feedback.append("Password length is good.")
    elif 8 <= len(password) < 12:
        score += 1
        feedback.append("Password length is decent but could be longer.")
    else:
        feedback.append("Password is too short. Consider making it at least 12 characters.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    # Check for digits
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add at least one digit (0-9).")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add at least one special character (e.g., !, @, #, $, etc.).")

    # Check for common patterns (e.g., '123456', 'password', 'abcdef', etc.)
    common_patterns = ['123456', 'password', 'abcdef', 'qwerty']
    if any(pattern in password.lower() for pattern in common_patterns):
        feedback.append("Avoid common patterns like '123456', 'password', etc.")
    else:
        score += 1  # Reward for avoiding common patterns

    # Calculate overall strength
    if score >= 7:
        strength = "Strong"
    elif 4 <= score < 7:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Return feedback and strength
    return strength, feedback

# Function to take user input and evaluate password
def main():
    print("Password Strength Assessment Tool")
    password = input("Enter a password to check its strength: ")
    strength, feedback = assess_password_strength(password)

    print("\nPassword Strength: " + strength)
    print("Feedback:")
    for suggestion in feedback:
        print("- " + suggestion)

# Run the main function
if __name__ == "__main__":
    main()
