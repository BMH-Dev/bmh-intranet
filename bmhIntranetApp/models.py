from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class QuickLinkTypes(models.Model):
    type_name = models.CharField(max_length=250)
    class Meta:
        verbose_name_plural = "Quick Link Types"
        
    def __str__(self):
        return self.type_name
    
    
class QuickLinks(models.Model):
    type_id = models.ForeignKey(QuickLinkTypes, on_delete=models.CASCADE)
    link_name = models.CharField(max_length=250)
    source_url = models.URLField()
    link_logo = models.ImageField()
    class Meta:
        verbose_name_plural = "Quick Links"
        
    def __str__(self):
        return self.link_name
    
    
class DocumentTypes(models.Model):
    type_name = models.CharField(max_length=250)
    class Meta:
        verbose_name_plural = "Document Types"
    def __str__(self):
        return self.type_name
    
    
class DocumentsRepository(models.Model):
    type_id = models.ForeignKey(DocumentTypes, on_delete=models.CASCADE)
    document_name = models.CharField(max_length=250)
    document_file = models.FileField()
    upload_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Documents Repository"
    
    def __str__(self):
        return self.document_name
    
class NewsTypes(models.Model):
    type_name = models.CharField(max_length=250)
    class Meta:
        verbose_name_plural = "News Types"
    def __str__(self):
        return self.type_name
    

class News(models.Model):
    type_id = models.ForeignKey(NewsTypes, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    descriptions = models.TextField()
    photo = models.ImageField()
    upload_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "News"
    
    def __str__(self):
        return self.title
    
    
class TrainingResources(models.Model):
    title = models.CharField(max_length=250)
    source_url = models.URLField()
    
    class Meta:
        verbose_name_plural = "Training Resources"
    
    def __str__(self):
        return self.title
        
    
class BmhCalendars(models.Model):
    event_name = models.CharField(max_length=250)
    descriptions = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    #start_time = models.TimeField()
    #end_time = models.TimeField()
    
    class Meta:
        verbose_name_plural = "BMH Calendars"
    
    def __str__(self):
        return f'{ self.event_name}'
    

class Announcements(models.Model):
    description = models.TextField()
    photo = models.FileField()
    class Meta:
        verbose_name_plural = "Announcements"
    def __str__(self):
        return self.description[:50]
    
    
class BmhVMCs(models.Model):
    vision = models.TextField()
    mission = models.TextField()
    core_values = models.TextField()
    class Meta:
        verbose_name_plural = "BMH Vision, Mission, & Core Values"
    def __str__(self):
        return "BMH Vision, Mission, & Core Values"
    
class Departments(models.Model):
    department_name = models.CharField(max_length=250)
    class Meta:
        verbose_name_plural = "Departments"
    def __str__(self):
        return self.department_name
    
    
class Designations(models.Model):
    title = models.CharField(max_length=250)
    department_id = models.ForeignKey(Departments, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Designation"
    
    def __str__(self):
        return self.title
        
 

class CustomUser(AbstractUser):
    user_type_data = (('1','HOD'), ('2', 'Staff'))
    user_type = models.CharField(default=2, max_length=10, choices=user_type_data)
    email = models.EmailField(unique=True)
    class Meta:
        verbose_name = "Custom User"
    
    def __str__(self):
        return self.username
        


class AdminHOD(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    depart_id = models.ForeignKey(Departments, on_delete=models.CASCADE)
    designation_id = models.ForeignKey(Designations, on_delete=models.CASCADE)
    profile_pic = models.ImageField(blank=True, null=True, default='')
    class Meta:
        verbose_name = "Admin HOD"
        verbose_name_plural = "Admin HODs"
    def __str__(self):
        return self.admin.username
    
class Staffs(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    department_id = models.ForeignKey(Departments, on_delete=models.CASCADE)
    designation_id = models.ForeignKey(Designations, on_delete=models.CASCADE)
    profile_pic = models.ImageField(blank=True, null=True, default='')
    class Meta:
        verbose_name = "Staffs"
        verbose_name_plural = "Staffs"
    def __str__(self):
        return self.admin.username
    

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == '1':
            AdminHOD.objects.create(admin=instance)
        if instance.user_type == '2':
            Staffs.objects.create(admin=instance)
            
@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == '1' and hasattr(instance, 'adminhod'):
        instance.adminhod.save()
    elif instance.user_type == '2' and hasattr(instance, 'staffs'):
        instance.staffs.save()