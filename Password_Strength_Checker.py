import re

def check_password_strength(password):
    # Criteria for a strong password
    length_check = len(password) >= 8
    lowercase_check = re.search(r'[a-z]', password)
    uppercase_check = re.search(r'[A-Z]', password)
    number_check = re.search(r'[0-9]', password)
    special_char_check = re.search(r'[@#$%^&+=]', password)

    # Feedback messages based on checks
    feedback = []
    
    if not length_check:
        feedback.append("Password should be at least 8 characters long.")
    if not lowercase_check:
        feedback.append("Password should contain at least one lowercase letter.")
    if not uppercase_check:
        feedback.append("Password should contain at least one uppercase letter.")
    if not number_check:
        feedback.append("Password should contain at least one number.")
    if not special_char_check:
        feedback.append("Password should contain at least one special character (@#$%^&+=).")

    # Check if password meets all the criteria
    if length_check and lowercase_check and uppercase_check and number_check and special_char_check:
        return "Strong password! Well done!"
    else:
        return "\n".join(feedback)

# Example usage
password = input("Enter your password: ")
print(check_password_strength(password))
