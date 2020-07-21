from django.db import models

# for each person who is in line
class LineMember(models.Model):
    name = models.CharField(maxlength=30)
    time = models.DateTimeField(auto_now=True)

