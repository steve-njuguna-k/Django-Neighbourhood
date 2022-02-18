from django.test import TestCase
from .models import NeighbourHood, Business, Profile
from django.contrib.auth.models import User

user = User.objects.get(id=1)
profile = Profile.objects.get(id=1)

# Create your tests here.
class TestNeighbourhood(TestCase):
    def setUp(self):
        self.new_neigbourhood=NeighbourHood(title = "Title", location="Langata", county='Naitobi', neighbourhood_logo="default.jpg", neighbourhood_admin=user)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_neigbourhood,NeighbourHood))

    def test_save_image(self):
        new_hood=self.new_neigbourhood
        new_hood.create_neigbourhood()
        posts=NeighbourHood.get_neighbourhoods()
        self.assertTrue(len(posts)>0)

    def update_image(self):
        new_hood=self.new_neigbourhood
        new_hood.update_neighbourhood()
        posts=NeighbourHood.get_neighbourhoods()
        self.assertTrue(len(posts)==0)

    def test_delete_image(self):
        new_hood=self.new_neigbourhood
        new_hood.delete_neigbourhood()
        posts=NeighbourHood.get_neighbourhoods()
        self.assertTrue(len(posts)==0)

class TestBusiness(TestCase):
    def setUp(self):
        self.new_business=Business(name = "Title", description="Langata", email='Naitobi', neighbourhood="default.jpg", owner=profile)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_business,Business))

    def test_save_image(self):
        new_biz=self.new_business
        new_biz.create_business()
        posts=Business.get_businesses()
        self.assertTrue(len(posts)>0)

    def update_image(self):
        new_biz=self.new_business
        new_biz.update_business()
        posts=Business.get_businesses()
        self.assertTrue(len(posts)==0)

    def test_delete_image(self):
        new_biz=self.new_business
        new_biz.delete_business()
        posts=Business.get_businesses()
        self.assertTrue(len(posts)==0)