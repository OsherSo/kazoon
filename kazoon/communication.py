import smtplib


def send_email_gmail(from_name, to_mail, subject, content, user, password):
    from email.message import EmailMessage
    email = EmailMessage()
    email["from"] = from_name
    email["to"] = to_mail
    email["subject"] = subject
    email.set_content(content)

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(user, password)
        smtp.send_message(email)


send_email_gmail("Osher", "solimani.osher@gmail.com", "Hello", "My name is osher", "solimani.osher@gmail.com",
                 "sxzxqpqigpuwdwoq")
