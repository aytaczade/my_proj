from django.db import models


class Author(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    image=models.ImageField(upload_to='authors')
    desctiption=models.TextField()
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    
    class Meta:
        verbose_name='Yazar'
        verbose_name_plural='Yazarlar'
        

class Category(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name='Kateqoriya'
        verbose_name_plural='Kateqoriyalar'
        
        
class Blog(models.Model):
    title=models.CharField(max_length=255)
    body=models.TextField(null=True, blank=True)
    image=models.ImageField(upload_to='blogs')
    author=models.ForeignKey(
        'blog.Author',
        on_delete=models.CASCADE,
        related_name='blogs'
    )
    slug=models.SlugField(unique=True)
    category=models.ManyToManyField(
        'blog.Category',
        related_name='blogs',
        
    )
    created_at=models.DateField(auto_now_add=True, null=True,blank=True)
    update_at=models.DateField(auto_now=True, null=True, blank=True)
    
    
        
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name='Bloq'
        verbose_name_plural='Bloqlar'
    
    