from bottle import post, request
import x
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


@post("/api-delete-user")
def send_delete_user_email():
    # cookie_user = {
    #     "user_email" : "emiliefdhansen@hotmail.com",
    #     "user_id" : "1234"
    # }
    # return cookie_user["user_id"]
    cookie_user = request.get_cookie("user", secret=x.COOKIE_SECRET)
    print (cookie_user)

    sender_email = "emiliefdhansen@gmail.com"
    receiver_email = cookie_user["user_email"]
    password = "esjgiseftxpubqus"

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = f"""\
    Hi,
    How are you?
    www.your_website_here.com"""
    html = f"""\
    <html>
      <body>
        <p>Hi,<br>
          How are you?<br>
          <a href="http://127.0.0.1:5009/delete_user/{cookie_user['user_id']}">Click here to delete your account</a>
        </p>
      </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

