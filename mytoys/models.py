from django.db import models

# Create your models here.
class Toy(models.Model):
    created=models.DateTimeField()
    name=models.CharField(max_length=150, blank=True, default='')
    description=models.CharField(max_length=250, blank=True, default='')
    toy_category=models.CharField(max_length=250, blank=False, default='')
    release_date=models.DateTimeField()
    was_included_in_home=models.BooleanField(default=False)
    
    
    
    class Meta:
        ordering=('name',)
    
       