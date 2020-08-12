from django.db import models

# Create your models here.


class Category(models.Model):
    """ Model representation for blog post categpries."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, unique=True,
                            verbose_name='Category name')

    def __str__(self):
        return self.name



