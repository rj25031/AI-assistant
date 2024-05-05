import smtplib
from email.message import EmailMessage

def send_email(to, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = "yashdalvi23903@gmail.com"
    msg['To'] = to

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Start TLS encryption
            server.login('pritannari@gmail.com', 'ugtophsrmkbbtwdu')
            server.send_message(msg)
            print("Email sent successfully!")
            return "Email sent successfully!"
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Failed to send the email."

