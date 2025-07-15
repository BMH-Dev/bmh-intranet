from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class QuickLinkTypes(models.Model):
    type_name = models.CharField(max_length=250)
    
    
class QuickLinks(models.Model):
    type_id = models.ForeignKey(QuickLinkTypes, on_delete=models.CASCADE)
    link_name = models.CharField(max_length=250)
    source_url = models.URLField()
    link_logo = models.ImageField()
    
    
class DocumentTypes(models.Model):
    type_name = models.CharField(max_length=250)
    
    
class DocumentsRepository(models.Model):
    type_id = models.ForeignKey(DocumentTypes, on_delete=models.CASCADE)
    document_name = models.CharField(max_length=250)
    
    
class NewsTypes(models.Model):
    type_name = models.CharField(max_length=250)
    

class News(models.Model):
    type_id = models.ForeignKey(NewsTypes, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    descriptions = models.TextField()
    photo = models.ImageField()
    
    
class TrainingResources(models.Model):
    title = models.CharField(max_length=250)
    source_url = models.URLField()
    
class BmhCalendars(models.Model):
    event_name = models.CharField(max_length=250)
    descriptions = models.TextField()
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    

class Announcements(models.Model):
    description = models.TextField()
    photo = models.FileField()
    
class BmhVMCs(models.Model):
    vision = models.TextField()
    mission = models.TextField()
    core_values = models.TextField()
    
class Departments(models.Model):
    department_name = models.CharField(max_length=250)
    
    
class Designations(models.Model):
    title = models.CharField(max_length=250)
    department_id = models.ForeignKey(Departments, on_delete=models.CASCADE)
 

class CustomUser(AbstractUser):
    user_type_data = ((1,'HOD'), ('2', 'Staff'))
    user_type = models.CharField(default=2, max_length=10, choices=user_type_data)
    email = models.EmailField(unique=True)


class AdminHOD(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    depart_id = models.ForeignKey(Departments, on_delete=models.CASCADE)
    designation_id = models.ForeignKey(Designations, on_delete=models.CASCADE)
    profile_pic = models.ImageField(blank=True, null=True, default='')
    
class Staffs(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    department_id = models.ForeignKey(Departments, on_delete=models.CASCADE)
    designation_id = models.ForeignKey(Designations, on_delete=models.CASCADE)
    profile_pic = models.ImageField(blank=True, null=True, default='')
    

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == '1':
            AdminHOD.objects.create(admin=instance)
        if instance.user_type == '2':
            Staffs.objects.create(admin=instance)
            
@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == '1':
        instance.adminhod.save()
    if instance.user_type == '2':
        instance.adminhod.save()