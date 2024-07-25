from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default='', blank=True, max_length=350)
    tag = models.CharField(max_length=50, default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images')
    link_to = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return f"{self.title}"

class Parents(models.Model):
    text = models.CharField(max_length=100, default='')
    link = models.CharField(max_length=255, default='')

class LeadNews(models.Model):
    created_at = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='images')

class Theme(models.Model):
    name = models.CharField(max_length=100)
    css_path = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Withoutborders(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default='', blank=True, max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    link_to = models.CharField(max_length=255,blank=True)
    days = models.CharField(max_length=255, blank=True)
    
class Firstday(models.Model):
    image = models.ImageField(upload_to='images')

class Secondday(models.Model):
    image = models.ImageField(upload_to='images')

class Thirdday(models.Model):
    image = models.ImageField(upload_to='images')

class Fourthday(models.Model):
    image = models.ImageField(upload_to='images')

class Fiftday(models.Model):
    image = models.ImageField(upload_to='images')