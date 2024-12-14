import re

def check_password_strength(password):
    # Initialize criteria flags
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[@$!%*?&]', password) is not None

    # Count the number of criteria met
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    # Determine password strength
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Prepare feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password must be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password must contain at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password must contain at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password must contain at least one number.")
    if not special_char_criteria:
        feedback.append("Password must contain at least one special character (e.g., @$!%*?&).")

    return strength, feedback

def main():
    print("Password Strength Checker")

    while True:
        password = input("Enter a password to check its strength: ")
        strength, feedback = check_password_strength(password)

        print(f"Password Strength: {strength}")
        if feedback:
            print("Feedback:")
            for message in feedback:
                print(f"- {message}")
        else:
            print("Your password meets all the criteria!")

        another = input("Would you like to check another password? (Y/N): ").upper()
        if another != 'Y':
            print("Thank you for using it")
            break # This line was indented too far causing the IndentationError. Corrected indentation to align with the if statement.


if __name__ == "__main__":
    main()