from django.db import models
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created


# Create your models here.
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    # email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'),
    #                                                reset_password_token.key)

    print(f"\nReset password {reset_password_token.key}\n")
    # sendepasswordresetmail(reset_password_token.user, reset_password_token.key)


