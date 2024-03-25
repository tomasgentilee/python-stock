from email.message import EmailMessage
import ssl
import smtplib

def sendEmail(to, subject, body):
    
    email_emisor = 'validtest3640@gmail.com'
    password = 'fxjz mdsb znct nobz'
    email_receptor = f'{to}'

    subject = "Esto es un email de prueba"
    body = f"""
    {body}
    """

    em = EmailMessage()
    em['From'] = email_emisor
    em['To'] = email_receptor
    em['Subject'] = subject
    em.set_content(body)

    contexto = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
        smtp.login(email_emisor, password=password)
        smtp.sendmail(email_emisor, email_receptor, em.as_string())
    

if __name__ == "__main__":
    #sendEmail()
    pass