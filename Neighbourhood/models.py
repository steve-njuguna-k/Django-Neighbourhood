from sre_parse import CATEGORIES
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NeighbourHood(models.Model):
    title = models.CharField(max_length=150, verbose_name='Neighbourhood Title', null=True, blank=True)
    location = models.CharField(max_length=150, verbose_name='Neighbourhood Location', null=True, blank=True)
    neighbourhood_logo = models.ImageField(upload_to='Neighbourhood_Pics', default='', verbose_name='NeighbourHood Logo')
    neighbourhood_admin = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Neighbourhood Admin')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name_plural = 'NeighbourHoods'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')
    bio = models.TextField(max_length=254, blank=True, verbose_name='Bio')
    profile_picture = models.ImageField(upload_to='Prof_Pics', default='', verbose_name='Profile Pic')
    location = models.CharField(max_length=50, blank=True, null=True, verbose_name='Location')
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, null=True, blank=True, verbose_name='NeighbourHood')
    email_confirmed = models.BooleanField(default=False, verbose_name='Is Confirmed?')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')
    
    def __str__(self):
        return str(self.author)
    
    class Meta:
        verbose_name_plural = 'Profiles'

class Business(models.Model):
    name = models.CharField(max_length=150, verbose_name='Business Name', null=True, blank=True)
    description = models.TextField(blank=True, verbose_name='Description')
    email = models.CharField(max_length=150, verbose_name='Business Email Address', null=True, blank=True)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, verbose_name='NeighbourHood')
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Business Owner')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name_plural = 'Businesses'

class Post(models.Model):
    title = models.CharField(max_length=120, null=True, verbose_name='Post Title')
    description = models.TextField(null=True, verbose_name='Post Description')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Post Author')
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, verbose_name='Rlated NeighbourHood')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name_plural = 'Posts'