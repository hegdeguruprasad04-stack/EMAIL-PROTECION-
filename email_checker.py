import re

def check_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        print("✅ Valid email format")
    else:
        print("❌ Invalid email format")

email = input("Enter your email: ")
check_email(email)
