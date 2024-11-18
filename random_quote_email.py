# random_quote_email.py

import smtplib
import random

quotes = [
    "Believe in yourself!",
    "You can achieve anything you set your mind to.",
    "Every day is a second chance.",
    "Dream big and dare to fail."
]

def send_email(recipient_email):
    sender_email = "your_email@example.com"
    sender_password = "your_password"
    subject = "Daily Motivation"
    body = random.choice(quotes)
    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message)

# Sample usage
send_email("recipient_email@example.com")
