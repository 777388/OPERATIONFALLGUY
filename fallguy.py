import email
import imaplib
import os
import requests

# Connect to the Gmail server
mail = imaplib.IMAP4_SSL("imap.gmail.com")

# Login to your Gmail account
mail.login("your_email@gmail.com", "your_password")

# Select the inbox
mail.select("inbox")

while True:
    # Check for new emails
    status, messages = mail.search(None, "UNSEEN")
    messages = messages[0].split()

    # If there are new emails
    if len(messages) > 0:
        for message in messages:
            # Fetch the email
            status, data = mail.fetch(message, "(RFC822)")
            email_message = email.message_from_bytes(data[0][1])

            # Print the sender and subject of the email
            print("From: " + email_message["From"])
            print("Subject: " + email_message["Subject"])
            
            if "Sally" in email_message["From"] or "Sally" in email_message["Subject"]:
                # Prepare the login data
                login_data = {
                    "username": "your_username",
                    "password": "your_password"
                }

                # Perform the login
                login_response = requests.post("http://example.com/login", data=login_data)

                # Check if login was successful
                if login_response.status_code == 200:
                    print("Login successful")

                    # Prepare the POST data
                    post_data = {
                        "email": email_message["From"],
                        "subject": email_message["Subject"]
                    }

                    # Make the POST request
                    response = requests.post("http://example.com/your-endpoint", data=post_data)

                    # Print the response status
                    print("Response status: " + response.status_code)

                    # Execute the program
                    os.system("your_program.exe")
                else:
                    print("Login failed")
            else:
                print("Email does not contain the name Sally")
    else:
        # Wait for new emails
        time.sleep(60)

# Close the connection
mail.close()
mail.logout()
