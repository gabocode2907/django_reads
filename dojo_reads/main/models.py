from django.db import models
import re

# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]')

class UserManager(models.Manager):
    def registration_validator(self,postData):
        # ALL THE VALIDATION FOR THE FORM
        errors = {}
        if len(postData['name']) < 2:
            errors['name'] = "Invalid Name. Name must be at least 3 characters"
        if len(postData['alias']) < 2:
            errors['alias'] = "Invalid Alias. Alias must be at least 3 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Ivalid Email"
        if len(postData['password']) < 5:
            errors['passwrod'] = "Password must be at leaset 6 characters"
        if postData['password'] != postData['confirm_password']:
            errors['pw_match'] = "Password does not match"

class User(models.Model):
    name = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()