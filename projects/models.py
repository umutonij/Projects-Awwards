from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 30,null = True)
    description = models.TextField(null = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.image

    def delete_image(self):
        self.delete()

    def save_image(self):
        self.save()

    def update_description(self,new_description):
        self.image_description = new_description
        self.save()


    @classmethod
    def get_image(cls, id):
        image = cls.objects.get(id=id)
        return image

    
    
    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(name__icontains=search_term)
        return project