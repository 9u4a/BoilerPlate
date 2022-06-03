from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=15, primary_key=True)
    user_pw = models.CharField(max_length=20)
    user_name = models.CharField(max_length=12)
    user_phoneNumber = models.CharField(max_length=20, unique=True)
    user_Email = models.CharField(max_length=40, unique=True)
    user_Grade = models.CharField(max_length=10, default="user")
    user_RefreshToken = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = 'TB_USER'
