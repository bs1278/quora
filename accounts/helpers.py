from django.core.mail import send_mail


class WelcomeEmail:
    subject = "Welcome New User"
    body = "Welcome body text here"
    from_email = "welcome@gmil.com"

    @classmethod
    def send_email_to(cls, emails):
        send_mail(
            cls.subject,
            cls.body,
            cls.from_email,
            emails
        )