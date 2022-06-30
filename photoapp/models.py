from django.db import models


class PhotoRepo(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    profile = models.ImageField(null=True, blank=True, default='default.jpg')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']
