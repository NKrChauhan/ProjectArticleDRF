from django.db import models
from commons.models.abstract_date_time import AbstractModelWithTimeStamps
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    def create(self, email, password=None):
        if not email:
            raise ValueError("User model must have email")
        user_obj = self.model(
            email=self.normalize_email(email),
        )
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user_obj = self.create(
            email=email, password=password
        )
        user_obj.staff = True
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, email, password=None):
        user_obj = self.create_staffuser(
            email=email, password=password
        )
        user_obj.admin = True
        user_obj.save(using=self._db)
        return user_obj


class User(AbstractBaseUser, AbstractModelWithTimeStamps):
    email = models.EmailField(max_length=255, unique=True,)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    def has_perm(self, perm, obj=None):
        # "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        # "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super(User, self).save(*args, **kwargs)
