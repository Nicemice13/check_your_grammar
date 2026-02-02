from django.db import models
from django.contrib.auth.models import User

class Content(models.Model):
    LANGUAGE_CHOICES = [
        ('ru', 'Русский'),
        ('en', 'Английский'),
        ('zh', 'Китайский'),
        ('es', 'Испанский'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contents')
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    corrected_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.language} - {self.created_at}"
