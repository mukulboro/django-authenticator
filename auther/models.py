from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class ExtendedUser(AbstractUser):
    # Extending default user model to have flag indicating if 2FA is enabled or not
    has_2fa = models.BooleanField(default=False)

