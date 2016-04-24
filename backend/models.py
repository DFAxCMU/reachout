from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here

class Organization(models.Model): 
    name = models.CharField(max_length=50, default="")
    location = models.CharField(max_length=50, default="")

class User(models.Model):
    name = models.CharField(max_length=50, default="")
    role = models.CharField(max_length=50, default="")
    org = models.ForeignKey(Organization, related_name="user")

class Client(models.Model): 
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    nick_name = models.CharField(max_length=50, default="")
    location = models.CharField(max_length=50, default="")
    visual_description = models.CharField(max_length=200, default="")
    org = models.ForeignKey(Organization, related_name="client_org")
    case_manager = models.ForeignKey(User, related_name="client_cm")
    followers = models.ManyToManyField(User, related_name="client_followers")
    is_military = models.BooleanField(default=False)
    # age_group (int or ranges?)
    duration_of_homelessness = models.IntegerField(default=0) # months?
    health_concerns = models.BooleanField(default=False)
    dna_assistance = models.BooleanField(default=False)
    has_doctor = models.BooleanField(default=False)
    has_insurance = models.BooleanField(default=False)
    def __str__(self): 
        return self.first_name
    def get_tags(self): 
        full_tags_list   = Tag.objects.all()
        tags_list   = []
        for tag in full_tags_list: 
            if (self in tag.client.all()):
                if (tag.name.lower() not in tags_list): 
                    tags_list.append(tag.name.lower())
        return tags_list
    def tags_list(self): 
        return ", ".join([t for t in self.get_tags()])
    # profile picture

class Route(models.Model):
    user = models.ForeignKey(User, related_name="user_route")
    client = models.ManyToManyField(Client, related_name="client_route")
    location = models.CharField(max_length=50, default="")
    radius = models.IntegerField(default=1) # miles?
    created_timestamp = models.DateTimeField(default=timezone.now)
    # start_timestamp = ?
    # end_timestamp = ?  

class Interaction(models.Model): 
    user = models.ForeignKey(User, related_name="interaction_user")
    client = models.ForeignKey(Client, related_name="interaction_client")
    location = models.CharField(max_length=50, default="")
    timestamp = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=200, default="")
    # audio recording
    route = models.ForeignKey(Route, related_name="interaction_route")

class Warehouse(models.Model): 
    org = models.OneToOneField(Organization, related_name="warehouse")

class Item(models.Model): 
    name = models.CharField(max_length=50, default="")
    warehouse = models.ForeignKey(Warehouse, related_name="warehouse_item")
    amount = models.IntegerField(default=0)

class Requests(models.Model): 
    src_interaction = models.ForeignKey(Interaction, related_name="request_src")
    comp_interaction = models.ForeignKey(Interaction, related_name="request_comp")
    asked_timestamp = models.DateTimeField(default=timezone.now)
    # completed_timestamp = ?
    item = models.ForeignKey(Item, related_name="request")
    amount = models.IntegerField(default=0)
    client_profile = models.ForeignKey(Client, related_name="request")
    description = models.CharField(max_length=200, default="")


class Tag(models.Model): 
    client = models.ManyToManyField(Client, related_name="client_tag")
    name = models.CharField(max_length=50, default="")
    tag_type = models.CharField(max_length=50, default="")
    def __str__(self): 
        return self.name
    # image

class Interaction_Photos(models.Model): 
    interaction = models.ForeignKey(Interaction, related_name="interaction_photos")
    # images

class Route_Item_Amounts(models.Model): 
    item  = models.ManyToManyField(Item, related_name="route_item")
    route = models.ManyToManyField(Route, related_name="route")
    amount = models.IntegerField(default=0)


