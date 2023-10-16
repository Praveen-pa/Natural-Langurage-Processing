import re

def main():
    # Sample text
    text = "Hello, my email addresses are example1@example.com and example2@example.com."

    # Define a regular expression pattern to match email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Find all email addresses in the text
    email_addresses = re.findall(email_pattern, text)

    # Print the email addresses found
    print("Email addresses found:")
    for email in email_addresses:
        print(email)

if __name__ == "__main__":
    main()