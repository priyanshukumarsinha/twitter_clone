from django.db import models

class login(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    # def __str__(self):
    #     return self.username