from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    short = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    image = models.FileField(upload_to='image',blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
 

class NewsImage(models.Model):
    image = models.FileField(upload_to='images')
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return self.image.url


LAW_TYPES = (
    (1, 'Действуещее законадательство'),
    (2, 'Проекты'),
    (3, 'Проекты_1'),
    (4, 'Проекты_2'),
)


class Law(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    type = models.IntegerField(choices=LAW_TYPES, default=1)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


PUBLICATION_TYPES = (
    (1, 'ICNL'),
    (2, 'Другие'),

)


class Publication(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    type = models.IntegerField(choices=LAW_TYPES, default=1)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

#код для избранный
#______________________________________________________________________________________________________

class NewsFovourite(models.Model):
    news=models.ForeignKey(News,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.news.title

class LawsFovourite(models.Model):
    laws=models.ForeignKey(Law,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.laws.title
class PublicaFovourite(models.Model):
    publica=models.ForeignKey(Publication,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.publica.title
#____________________________________________________________________________________________________________




