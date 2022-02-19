from django.db import models
from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField

COUNTIES = [
    ('', ('Choose')), 
    ('Baringo', ('Baringo')),
    ('Bomet', ('Bomet')),
    ('Bungoma ', ('Bungoma ')),
    ('Busia', ('Busia')),
    ('Elgeyo Marakwet', ('Elgeyo Marakwet')),
    ('Embu', ('Embu')),
    ('Garissa', ('Garissa')),
    ('Homa Bay', ('Homa Bay')),
    ('Isiolo', ('Isiolo')),
    ('Kajiado', ('Kajiado')),
    ('Kakamega', ('Kakamega')),
    ('Kericho', ('Kericho')),
    ('Kiambu', ('Kiambu')),
    ('Kilifi', ('Kilifi')),
    ('Kirinyaga', ('Kirinyaga')),
    ('Kisii', ('Kisii')),
    ('Kisumu', ('Kisumu')),
    ('Kitui', ('Kitui')),
    ('Kwale', ('Kwale')),
    ('Laikipia', ('Laikipia')),
    ('Lamu', ('Lamu')),
    ('Machakos', ('Machakos')),
    ('Makueni', ('Makueni')),
    ('Mandera', ('Mandera')),
    ('Meru', ('Meru')),
    ('Migori', ('Migori')),
    ('Marsabit', ('Marsabit')),
    ('Mombasa', ('Mombasa')),
    ('Muranga', ('Muranga')),
    ('Nairobi', ('Nairobi')),
    ('Nakuru', ('Nakuru')),
    ('Nandi', ('Nandi')),
    ('Narok', ('Narok')),
    ('Nyamira', ('Nyamira')),
    ('Nyandarua', ('Nyandarua')),
    ('Nyeri', ('Nyeri')),
    ('Samburu', ('Samburu')),
    ('Siaya', ('Siaya')),
    ('Taita Taveta', ('Taita Taveta')),
    ('Tana River', ('Tana River')),
    ('Tharaka Nithi', ('Tharaka Nithi')),
    ('Trans Nzoia', ('Trans Nzoia')),
    ('Turkana', ('Turkana')),
    ('Uasin Gishu', ('Uasin Gishu')),
    ('Vihiga', ('Vihiga')),
    ('Wajir', ('Wajir')),
    ('West Pokot', ('West Pokot')),
]

CHOICES = [
    ('1', 'Crimes and Safety'),
    ('2', 'Health Emergency'),
    ('3', 'Recommendations'),
    ('4', 'Fire Breakouts'),
    ('5', 'Lost and Found'),
    ('6', 'Death'),
    ('7', 'Event'),
]

# Create your models here.
class NeighbourHood(models.Model):
    title = models.CharField(max_length=150, verbose_name='Neighbourhood Title', null=True, blank=True)
    description = models.TextField(max_length=254, blank=True, verbose_name='Description')
    location = models.CharField(max_length=150, verbose_name='Neighbourhood Location', null=True, blank=True)
    county = models.CharField(choices=COUNTIES, max_length=150, verbose_name='Neighbourhood County', null=True, blank=True)
    #neighbourhood_logo = CloudinaryField('neighbourhood_logo')
    neighbourhood_logo = models.ImageField(upload_to='Neighbourhood-Logo', verbose_name='Neighbourhood-Logo')
    neighbourhood_admin = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Neighbourhood Admin')
    health_department = models.CharField(max_length=15, null=True, blank=True, verbose_name='Health Department')
    police_department = models.CharField(max_length=15, null=True, blank=True, verbose_name='Police Department')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

    def get_neighbourhoods(self):
        neighbourhoods = NeighbourHood.objects.all()
        return neighbourhoods
    
    def create_neigbourhood(self):
        self.save()

    def delete_neigbourhood(self):
        self.delete()

    def find_neigbourhood(self,neigborhood_id):
        neigbourhood = NeighbourHood.objects.filter(self = neigborhood_id)
        return neigbourhood

    def update_neighborhood(self, id, title, location, county, neighbourhood_logo):
        update = NeighbourHood.objects.filter(id = id).update(title = title , location = location, county = county, neighbourhood_logo = neighbourhood_logo)
        return update

    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name_plural = 'NeighbourHoods'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')
    bio = models.TextField(max_length=254, blank=True, verbose_name='Bio')
    national_id = models.CharField(max_length=10, blank=True, verbose_name='National ID')
    #profile_picture = CloudinaryField('profile_picture')
    profile_picture = models.ImageField(upload_to='Profile-Pics', verbose_name='Profile-Pics')
    neighbourHood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, null=True, blank=True, verbose_name='NeighbourHood')
    email_confirmed = models.BooleanField(default=False, verbose_name='Is Confirmed?')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')
    
    def __str__(self):
        return str(self.user.username)
    
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

    def get_businesses(self):
        businesses = Business.objects.all()
        return businesses

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def find_business(self,business_id):
        business = Business.objects.filter(self = business_id)
        return business

    def update_business(self, id, name, description, email, neighbourhood):
        update = NeighbourHood.objects.filter(id = id).update(name = name , description = description, email = email, neighbourhood = neighbourhood)
        return update
    
    class Meta:
        verbose_name_plural = 'Businesses'

class Post(models.Model):
    title = models.CharField(max_length=120, null=True, verbose_name='Post Title')
    description = models.TextField(null=True, verbose_name='Post Description')
    category = models.CharField(max_length=120, choices=CHOICES, verbose_name='Post Category')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Post Author')
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, verbose_name='Rlated NeighbourHood')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name_plural = 'Posts'

class Membership(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='User')
    neighbourhood_membership = models.ForeignKey(NeighbourHood, related_name='neighbourhood_member', on_delete=models.CASCADE, verbose_name='NeighbourHood')

    def __str__(self):
        return str(self.user.username + '-' + self.neighbourhood_membership.title)
    
    class Meta:
        verbose_name_plural = 'Memberships'