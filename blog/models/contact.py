from django.db import models

class ContactModel(models.Model):
    email = models.EmailField(max_length=250)
    nama_surname = models.CharField(max_length=150)
    message = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'Contact'
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'
        
    def __str__(self):
        return self.email

