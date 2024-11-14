import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(body, receiver_email, subject=""):

    sender_email = "somayarora8008@gmail.com"
    sender_password = "ggsnzpnuclyldxpb"
    display_name = "J.A.R.V.I.S."

    msg = MIMEMultipart()
    msg['From'] = f"{display_name} <{sender_email}>"
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        server.login(sender_email, sender_password)

        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")

    finally:
        server.quit()

# Example usage
body = "This is a test email sent from J.A.R.V.I.S."
receiver_email = "arorasanjanaarora31@gmail.com"

send_email(body, receiver_email)