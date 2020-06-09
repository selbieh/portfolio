from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class About(models.Model):
    name		 = models.CharField(max_length=200)
    address		 = models.CharField(max_length=200)
    mobile	 	 = models.CharField(max_length=200)
    email        = models.EmailField(blank=True)
    description	 = RichTextField()

    def __str__(self):
        return self.name


class Experience(models.Model):
    title	 = models.CharField(max_length=200)
    company	 = models.CharField(max_length=200)
    date 	 = models.CharField(max_length=200)
    summery  = RichTextField()

    def __str__(self):
        return self.title



class Project(models.Model):
    title 		= models.CharField(max_length=200)
    image 		= models.ImageField(upload_to='static/img', null=True)
    description = RichTextField()
    link		= models.URLField()
    link_back    = models.URLField(null=True , blank=True )
    code_link   = models.URLField(null=True)

    def __str__(self):
        return self.title


class CV(models.Model):
    cv_file = models.URLField()


