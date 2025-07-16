from django.contrib import admin
from .models import QuickLinkTypes, QuickLinks, DocumentTypes, DocumentsRepository, NewsTypes, News, TrainingResources, BmhCalendars, Announcements, BmhVMCs, Departments, Designations, CustomUser,Staffs, AdminHOD


# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    CustomUser, AdminHOD, Staffs,
    QuickLinkTypes, QuickLinks, DocumentTypes, DocumentsRepository,
    NewsTypes, News, TrainingResources, BmhCalendars,
    Announcements, BmhVMCs, Departments, Designations
)

# customization for CustomUser
admin.site.site_header = 'BMH Intranet Admin'
admin.site.site_title = 'BMH Intranet Admin Portal'
admin.site.index_title = 'Welcome to BMH Intranet Admin Portal'

# Registering CustomUser with custom display
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'user_type', 'is_staff', 'is_active']
    search_fields = ['username', 'email']
    list_filter = ['user_type', 'is_staff', 'is_superuser', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        ('User Type Info', {'fields': ('user_type',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('User Type Info', {'fields': ('user_type',)}),
    )

# Register AdminHOD
@admin.register(AdminHOD)
class AdminHODAdmin(admin.ModelAdmin):
    list_display = ['admin', 'depart_id', 'designation_id']
    search_fields = ['admin__username', 'depart_id__department_name']
    list_filter = ['depart_id', 'designation_id']

# Register Staffs
@admin.register(Staffs)
class StaffsAdmin(admin.ModelAdmin):
    list_display = ['admin', 'department_id', 'designation_id']
    search_fields = ['admin__username', 'department_id__department_name']
    list_filter = ['department_id', 'designation_id']

    

@admin.register(QuickLinkTypes)
class QuickLinkTypesAdmin(admin.ModelAdmin):
    list_display = ['type_name']
    search_fields = ['type_name']
    list_filter = ['type_name']
    
@admin.register(QuickLinks)
class QuickLinksAdmin(admin.ModelAdmin):
    list_display = ['link_name', 'source_url', 'type_id']
    search_fields = ['link_name', 'source_url']
    list_filter = ['type_id']

@admin.register(DocumentTypes)
class DocumentTypesAdmin(admin.ModelAdmin):
    list_display = ['type_name']
    search_fields = ['type_name']
    list_filter = ['type_name']

@admin.register(DocumentsRepository)
class DocumentsRepositoryAdmin(admin.ModelAdmin):
    list_display = ['document_name', 'type_id']
    search_fields = ['document_name']
    list_filter = ['type_id']

@admin.register(NewsTypes)
class NewsTypesAdmin(admin.ModelAdmin):
    list_display = ['type_name']
    search_fields = ['type_name']
    list_filter = ['type_name'] 

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'type_id', 'descriptions']
    search_fields = ['title', 'descriptions']
    list_filter = ['type_id']

@admin.register(TrainingResources)
class TrainingResourcesAdmin(admin.ModelAdmin):
    list_display = ['title', 'source_url']
    search_fields = ['title', 'source_url']
    list_filter = ['title']

@admin.register(BmhCalendars)
class BmhCalendarsAdmin(admin.ModelAdmin):
    list_display = ['event_name', 'start_date', 'end_date']
    search_fields = ['event_name', 'descriptions']
    list_filter = ['start_date', 'end_date']

@admin.register(Announcements)
class AnnouncementsAdmin(admin.ModelAdmin):
    list_display = ['description', 'photo']
    search_fields = ['description']
    list_filter = ['description']

@admin.register(BmhVMCs)
class BmhVMCsAdmin(admin.ModelAdmin):
    list_display = ['vision', 'mission', 'core_values']
    search_fields = ['vision', 'mission', 'core_values']
    list_filter = ['vision', 'mission', 'core_values']

@admin.register(Departments)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ['department_name']
    search_fields = ['department_name']
    list_filter = ['department_name']
    
    @admin.register(Designations)
    class DesignationsAdmin(admin.ModelAdmin):
        list_display = ['title', 'department_id']
        search_fields = ['title']
        list_filter = ['department_id']