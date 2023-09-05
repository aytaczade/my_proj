from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.full_name} - {self.email}'
    
    class Meta:
        verbose_name = 'Müraciət'
        verbose_name_plural = 'Müraciətlər'
