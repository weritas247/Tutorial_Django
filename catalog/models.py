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
  date_of_death = models.DateField("Died", null=True, blank=True)

  class Meta:
    ordering = ["last_name", "first_name"]

  def __str__(self):
    return f"{self.last_name}, {self.first_name}"

class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
  summary = models.TextField(max_length=1000, help_text="책의 설명을 입력하세요")
  isbn = models.CharField(
    "ISBN",
     max_length=13,
     help_text="13자리 ISBN을 입력하세요")
  genre = models.ManyToManyField(Genre, help_text="책의 장르를 고르세요")

  def __str__(self):
      return self.title