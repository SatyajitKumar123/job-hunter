from django.db import models
from django.contrib.auth.models import User


class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('APPLIED', 'Applied'),
        ('INTERVIEW', 'Interviewing'),
        ('OFFER', 'Offer Received'),
        ('REJECTED', 'Rejected'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    company = models.CharField(max_length=100)
    postition = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='APPLIED')
    date_applied = models.DateField()
    
    def __str__(self):
        return f"{self.company} - {self.postition}"

    class Meta:
        ordering = ['-date_applied']