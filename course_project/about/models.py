from django.db import models

class About(models.Model):
    title=models.CharField(verbose_name='basliq', max_length=255)
    description=models.TextField(verbose_name='Metn')
    footer_description=models.TextField(verbose_name='footer-deki metn', null=True)
    image=models.ImageField('sekil', upload_to='about')
    
    
    def __str__(self):
        return 'About'
    
    
    class Meta:
        verbose_name="Haqqimizda"
        verbose_name_plural="Haqqimizda"
        
        
class AboutPoint(models.Model):
    about=models.ForeignKey(
        'about.About',
        on_delete=models.CASCADE,
        related_name='points',
    )
    title=models.CharField(max_length=255)
    description=models.TextField()   
    
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name="Haqqimizda punkt"
        verbose_name_plural="Haqqimizda punktlar" 
        
        
class Store(models.Model):
    name=models.CharField(default=0,max_length=255)
    address=models.TextField(default=0)
    email=models.EmailField(default=0)
    phone_number=models.CharField(default=0,max_length=255)
    optional_phone_number=models.CharField(default=0,max_length=255)
        
        
    def __str__(self):
        return 'Store'
    
    
    class Meta:
        verbose_name=" Magaza "
        verbose_name_plural=" Magazalar " 
        
class SocialMedia(models.Model):
    instagram = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    facebook = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    youtube = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    tiktok = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    linkedin = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Sosial media'
        verbose_name_plural = 'Sosial media'
        
        
        