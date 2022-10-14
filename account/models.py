from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from .manager import ManagerAccountUser


class ModelAccountUser(AbstractUser):

    username = None
    
    uid = models.UUIDField(default=uuid.uuid4,
                           unique=True,
                           editable=False,
                           help_text="Unique identification number for the user.")

    email = models.EmailField(
        max_length=225,
        unique=True,
        help_text="Email of the user."
    )


    objects = ManagerAccountUser()

    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = []

    # -------------------------------------------------------------------------
    # Meta
    # -------------------------------------------------------------------------
    class Meta:
        db_table = "account_user"
        verbose_name = "User"
        verbose_name_plural = "Users"


    # ---------------------------------------------------------------------------
    # __str__
    # ---------------------------------------------------------------------------
    def __str__(self):
        """
        Returns the string representation of the user object.
        """
        return self.email

    # ---------------------------------------------------------------------------
    # full_name
    # ---------------------------------------------------------------------------
    @property
    def full_name(self):
        """
        Method to return user's full name
        """

        if self.first_name and self.last_name:
            return "{} {}".format(self.first_name, self.last_name).title()
        else:
            return self.email