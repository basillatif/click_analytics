from django.db import models

# Create your models here.

class Slider(models.Model):
    image = models.ImageField(upload_to="slider_image")
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to="project_image")

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="testimonial_image")
    country = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="client_image")

    def __str__(self):
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.email

class Social(models.Model):
    facebook = models.URLField()
    twitter = models.URLField()
    linkin = models.URLField()
    github = models.URLField()
    instagram = models.URLField()

    def __str__(self):
        return str(self.id)