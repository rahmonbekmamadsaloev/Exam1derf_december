from django.db import models
from account.models import CustomUser

class Submission(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    )
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    task = models.ForeignKey('courses.Task',on_delete=models.CASCADE)
    code = models.TextField()
    score = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
