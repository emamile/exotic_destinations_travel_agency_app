# Importing the asyncio module.
import asyncio

from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from pydantic import EmailStr

from app.config import settings


# > This class is responsible for sending emails.
class EmailService:
    conf = ConnectionConfig(
        MAIL_USERNAME=settings.MAIL_USERNAME,
        MAIL_PASSWORD=settings.MAIL_PASSWORD,
        MAIL_PORT=settings.MAIL_PORT,
        MAIL_SERVER=settings.MAIL_SERVER,
        MAIL_FROM=settings.MAIL_FROM,
        MAIL_STARTTLS=False,
        MAIL_SSL_TLS=False,
    )

    @staticmethod
    def send_email(email: EmailStr):
        """
        It sends an email to the user.

        :param email: EmailStr - The email address you want to send the email to
        :type email: EmailStr
        :return: the message that was sent.
        """
        html = """<p>I said to her hi, hi, hi, hello!</p> """

        message = MessageSchema(
            subject="Someone logged into your account please check your activity log.",
            recipients=[email],
            body=html,
            subtype=MessageType.html,
        )

        fm = FastMail(EmailService.conf)
        asyncio.run(fm.send_message(message))

        return
