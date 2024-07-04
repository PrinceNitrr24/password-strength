import re

def password_strength(password):
    # Criteria for password strength
    length_criteria = len(password) >= 8
    digit_criteria = re.search(r"\d", password) is not None
    uppercase_criteria = re.search(r"[A-Z]", password) is not None
    lowercase_criteria = re.search(r"[a-z]", password) is not None
    special_char_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    # Strength counter
    strength = 0
    if length_criteria:
        strength += 1
    if digit_criteria:
        strength += 1
    if uppercase_criteria:
        strength += 1
    if lowercase_criteria:
        strength += 1
    if special_char_criteria:
        strength += 1

    # Evaluate strength
    if strength == 5:
        return "Very Strong"
    elif strength == 4:
        return "Strong"
    elif strength == 3:
        return "Moderate"
    elif strength == 2:
        return "Weak"
    else:
        return "Very Weak"

# Main function to take user input and check password strength
def main():
    password = input("Enter your password: ")
    strength = password_strength(password)
    print(f"Your password strength is: {strength}")

if __name__ == "__main__":
    main()
