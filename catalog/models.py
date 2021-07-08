from django.db import models

# Create your models here.
class Genre(models.Model):
  name = models.CharField(
    max_length=200,
    help_text="책의 장르를 입력하세요"
  )
  
  def __str__(self):
    return self.name

class Author(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  date_of_birth = models.DateField(null=True, blank=True)
  date_of_birth = models.DateField(null=True, blank=True)