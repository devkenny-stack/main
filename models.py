from django.db import models

class Admission(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    grade = models.CharField(max_length=50)
    message = models.TextField()
    date_applied = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
