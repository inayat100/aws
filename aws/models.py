from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=10)
    img = models.ImageField(upload_to='media')
    def __str__(self):
        return f'name= {self.name} ========= img = {self.img}'