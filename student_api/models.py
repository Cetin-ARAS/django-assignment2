from django.db import models

class Category(models.Model):
    id = models.IntegerField(primary_key=True, blank=True, null=False)
     
    def __str__(self):
        return f"{self.id}"

class Post(models.Model):  
    category = models.ForeignKey(
        Category, related_name='students', on_delete=models.CASCADE)
    title = models.TextField()
    content = models.CharField(max_length=30)
    cotegory_id = models.IntegerField(blank=True, null=True)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} {self.content}"
