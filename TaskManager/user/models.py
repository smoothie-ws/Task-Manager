from django.contrib.auth.models import User
from django.db import models


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=False)
#     name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=50, blank=False)
#
#     def __str__(self):
#         return self.name
