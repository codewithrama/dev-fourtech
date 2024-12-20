import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Mailtrap SMTP configuration
SMTP_SERVER = "smtp.mailtrap.io"
SMTP_PORT = 587
SMTP_USERNAME = "b70035c6a55f2b"  # Replace with your Mailtrap username
SMTP_PASSWORD = "88506ccfeeedea"  # Replace with your Mailtrap password

# Email details
sender_email = "admin@fourtechnologies.in"
receiver_email = "ramasubramanian35427@gmail.com"
subject = "New Form Submission with Attachment"

# Create the email
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Email body
body = "You have a new form submission. Please see the attached file."
message.attach(MIMEText(body, "plain"))

# Add attachment
file_path = "src/docs/How_to_Find_The_Best_Employees_For_Your_Business_Guide.pdf"  # Replace with the file path
file_name = "How_to_Find_The_Best_Employees_For_Your_Business_Guide.pdf"

try:
    with open(file_path, "rb") as attachment:
        # Load file content and encode it
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {file_name}",
        )
        message.attach(part)
except FileNotFoundError:
    print("Attachment not found, sending email without attachment.")

# Connect to Mailtrap's SMTP server
try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()  # Upgrade the connection to secure
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
