from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class userProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    about = models.TextField(null=True)
    email = models.CharField(max_length=200,)
    country = models.CharField(max_length=200,null=True)
    place = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='book_media',null=True)
    age = models.IntegerField(null=True)
    contact = models.IntegerField(null=True)

   
    education = models.TextField(null=True)
 
    def __str__(self):
        return '{}'.format(self.name)


class userProject(models.Model):
    user = models.ForeignKey(userProfile,on_delete=models.CASCADE)
    work_experience = models.TextField(null=True)
    skills = models.CharField(max_length=200,null=True)
    cerifications = models.TextField(null=True)

    first_Project_Title = models.CharField(max_length=200,null=True)
    first_Project_Description = models.TextField(null=True)
    first_Project_Image = models.ImageField(upload_to='book_media',null=True)
    first_Project_Link = models.URLField(null=True)

    second_Project_Title = models.CharField(max_length=200,null=True)
    second_Project_Description = models.TextField(null=True)
    second_Project_Image = models.ImageField(upload_to='book_media',null=True)
    second_Project_Link = models.URLField(null=True)

    third_Project_Title = models.CharField(max_length=200,null=True)
    third_Project_Description = models.TextField(null=True)
    third_Project_Image = models.ImageField(upload_to='book_media',null=True)
    third_Project_Link = models.URLField(null=True)


    def __str__(self):
        return '{}'.format(self.user.username)