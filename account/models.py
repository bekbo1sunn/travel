from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager




class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email, password, phone, **kwargs):
        if not email:
            raise ValueError("Email is required")
        kwargs["is_active"] = True
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, phone=phone, **kwargs)
        # self.model = User
        user.set_password(password)  # хеширование пароля
        user.save(using=self._db)  # созраняем юзера в бд
        return user

    def create_superuser(self,username, email, password, phone, **kwargs):
        if not email:
            raise ValueError("Email is required")
        kwargs["is_staff"] = True  # даем права суперадмина
        kwargs["is_superuser"] = True
        kwargs["is_active"] = True
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, phone=phone, **kwargs)
        # self.model = User
        user.set_password(password)  # хеширование пароля
        user.save(using=self._db)  # созраняем юзера в бд
        return user
    


class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)  # когда регитр-ся чтобы выходило "Польз-ль с таким имененем уже сущ-ет
    phone = models.CharField(max_length=50)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    is_active = models.BooleanField(default=True)


    USERNAME_FIELD = 'username'    # указываем какое поле использовать при логине
    REQUIRED_FIELDS = ['email', 'phone']

    objects = UserManager()  # указываем нового менеджера


    

class Billing(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='billing'
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def top_up(self, amount):
        """Пополнение счета, если транзакция прошла успешно, вернется True"""
        if amount > 0:
            self.amount += amount
            self.save()
            return True
        return False

    def withdraw(self, amount):
        """Снятие денег со счета, если транзакция прошла успешно, вернется True"""
        if self.amount >= amount:
            self.amount -= amount
            self.save()
            return True
        return False

    def __str__(self):
        return self.user.username