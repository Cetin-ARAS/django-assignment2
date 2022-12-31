from django.db import models


class Category(models.Model):
    id = models.IntegerField(blank=True, null=True)
     
    def __str__(self):
        return f"{self.id}"

class Post(models.Model):  
    category = models.ForeignKey(
        Category, related_name='students', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=30)
    cotegory_id = models.IntegerField(blank=True, null=True)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.number}-{self.last_name} {self.first_name}"
