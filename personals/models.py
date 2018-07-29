from django.db import models


class Personal(models.Model):
    fullname = models.CharField(max_length=40)
    summary = models.TextField(max_length=200)
    email_id = models.EmailField()
    display_pic = models.ImageField(upload_to='images/', default='images/default.jpg')
    resume = models.FileField(upload_to='resume/')

    def __str__(self):
        return 'User : ' + self.fullname
