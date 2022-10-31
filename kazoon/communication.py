import smtplib
import requests
import hashlib


def send_email_gmail(from_name, to_mail, subject, content, user, password):
    """
        Sending an email through gmail.

        Arguments:
            from_name: The name of the message sender.
            to_mail: The email to which the message will be sent.
            subject: The subject of the message.
            content: The content of the message.

        Return:
            0 for a safe password. Otherwise, the number of times the password has been hacked in the past.
    """
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


def password_checker(password):
    """
        Checks if password is safe or not.

        Arguments:
            password: The password you want to check.

        Return:
            0 for a safe password. Otherwise, the number of times the password has been hacked in the past.
    """
    sha1_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, rest = sha1_password[:5], sha1_password[5:]

    url = "https://api.pwnedpasswords.com/range/" + first5_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}')

    res = (line.split(':') for line in res.text.splitlines())
    for h, count in res:
        if h == rest:
            return count

    return 0
