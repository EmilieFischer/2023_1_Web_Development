from bottle import post, request
import x
import uuid
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

@post("/send-forgot-password-email")
def _():
    try: 
      db = x.db()

      user_email = request.forms.get("user_email")

      user_reset_password_key = str(uuid.uuid4().hex)


      total_changes = db.execute("""
              UPDATE users
              SET user_reset_password_key = ?
              WHERE user_email = ?
          """, (user_reset_password_key, user_email)).rowcount
      
      db.commit()
      
      if not total_changes: raise Exception("Could not update user_reset_password_key.")

      # send email information
      sender_email = "emiliefdhansen@gmail.com"
      receiver_email = user_email
      password = "esjgiseftxpubqus"

      message = MIMEMultipart("alternative")
      message["Subject"] = "Reset password email"
      message["From"] = sender_email
      message["To"] = receiver_email

      # Create the plain-text and HTML version of your message
      text = f"""\
      Hi,
      Looks like you have forgotten the password. Lets help you get access to your account again by resetting your password. Click the link below to reset your password.
      www.your_website_here.com"""
      html = f"""\
      <html>
        <body>
        <p>Hi.
        <br>Looks like you have forgotten the password.
        <br>Lets help you get access to your account again by resetting your password.
        <br><a href="http://127.0.0.1:5009/resetpassword/{user_reset_password_key}">Click here to reset your password</a>.
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

      db.commit()
      return {"info":"ok"}
    except Exception as e:
        print(e)
        return {"info":str(e)}
    finally:
        if "db" in locals(): db.close()
