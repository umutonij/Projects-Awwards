from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 30,null = True)
    description = models.TextField(null = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
    	return self.title

    def delete_project(self):
    	self.delete()

    def save_project(self):
    	self.save()

    @classmethod
    def all_projects(cls):
        project = cls.objects.all()
        return projects 

    @classmethod
    def get_project(cls, id):
        project = cls.objects.get(id=id)
        return project
    
    def __str__(self):
    	return self.user.username

    
    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(name__icontains=search_term)
        return project