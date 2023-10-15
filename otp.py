import smtplib
import random
import string
otp=0
# Function to generate a random OTP
def generate_otp(length=6):
    characters = string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def g():
    global otp
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # Replace with the appropriate port for your email provider
    smtp_username = 'yashdhokane12@gmail.com'
    smtp_password = 'nwqhkkjfbjvsvlcj'

    # Sender and receiver email addresses
    sender_email = 'yashdhokane12@gmail.com'
    receiver_email = 'hulk.yt98@gmail.com'

    # Generate a random OTP
    otp = generate_otp()
    print("12",otp)

    # Email content
    subject = 'Your OTP Code'
    body = f'Your OTP code is: {otp}'
    message = f'Subject: {subject}\n\n{body}'

    # Try to send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, message)
        server.quit()
        print(f'OTP sent successfully to {receiver_email}',otp)
        return otp
    except Exception as e:
        print(f'Error sending OTP: {str(e)}')
        
g()
print(otp)