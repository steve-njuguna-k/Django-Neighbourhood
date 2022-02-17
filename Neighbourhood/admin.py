from django.contrib import admin
from .models import Profile, Post, NeighbourHood, Membership, Business

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(NeighbourHood)
admin.site.register(Membership)
admin.site.register(Business)