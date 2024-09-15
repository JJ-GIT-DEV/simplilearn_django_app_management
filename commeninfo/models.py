from django.db import models
from datetime import date
from django.core.exceptions import ValidationError

class UserInfo(models.Model):
    username = models.CharField("Username", max_length=50)
    email = models.EmailField("Email", blank=True)
    password = models.CharField("Password", max_length=50)
    password_re_type = models.CharField("Repeat Password", max_length=50)
    first_name = models.CharField("First Name", max_length=20)
    last_name = models.CharField("Last Name", max_length=20)
    uniqueID = models.IntegerField("Unique ID", unique=True)
    date_of_birth = models.DateField("Date Of Borth", auto_now_add=False, auto_now=False, blank=True)

    def __str__(self) -> str:
        return self.username

    def clean(self):
            # Checking fields according to different requirements...
            # Username cannot be empty and must be unique
            if self.username is None:
                print(self.username)
                raise ValidationError("The Username must not be empty.")
            else:
                username = self.username
                if UserInfo.objects.filter(username=username).exists():
                    raise ValidationError("The Username already exists!")
                    # Check that the two password entries match
            # Password cannot be empty and must be equal to password (re-type)
            if self.password is None and self.password_re_type is None:
                raise ValidationError("The Password must not be empty.")
            else:
                password = self.password
                password_re_type = self.password_re_type
                if password and password_re_type and password != password_re_type:
                    raise ValidationError("Passwords do not match.")
