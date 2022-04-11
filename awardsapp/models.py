
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default="")
    profilePhoto = CloudinaryField('images')
    bio = models.TextField()
    contact=models.CharField(max_length=300)
    
    
    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()
        
    @classmethod
    def get_profile(cls,id):
        profile = Profile.objects.all()
        return profile
        
    @classmethod
    def update_profile(cls,id):
        cls.objects.get(user_id=id)

    @classmethod
    def delete_profile(cls,id):
        cls.objects.filter(id).delete()


    @classmethod
    def search_by_name(cls, searched_name):  
        username = cls.objects.filter(username__icontains=searched_name)
        return username


     

class Post(models.Model):
    title = models.CharField(max_length=200)
    project_image = CloudinaryField('images')
    description =models.TextField()
    url=models.CharField(max_length=200)
    user= models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    profile=models.ForeignKey(Profile,on_delete= models.CASCADE,null=True)
    
    def __str__(self):
        return self.title

    def save_post(self):
        self.save()
    
    @classmethod
    def get_post_by_id(cls,id):
        post_per_id=cls.objects.filter(id = id).get()
        return post_per_id

    @classmethod
    def get_post(cls,i):
        profile = Profile.objects.all()
        return profile

    @classmethod
    def delete_post(cls,id):
        cls.objects.filter(id).delete()

    @classmethod
    def search_by_project(cls, searched_project):  
        project = cls.objects.filter(title__icontains=searched_project)
        return project





class Ratings(models.Model):
     RATE_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),)
     design=models.IntegerField("design",choices=RATE_CHOICES,)
     userbility=models.IntegerField("userbility",choices=RATE_CHOICES,)
     content=models.IntegerField("content",choices=RATE_CHOICES,)
     average = models.DecimalField("average",default=1, blank=False, decimal_places=2, max_digits=20)
     date = models.DateTimeField(default=timezone.now)
     post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
     user=models.ForeignKey(User,on_delete= models.CASCADE,null = True)

     def __str__(self):
        return str(self.post)

     @classmethod
     def rate_post(cls,id):
         cls.objects.filter(post=id).save()




