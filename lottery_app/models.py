from django.db import models

# Create your models here.
from django.db import models
from datetime import date

from django.template.defaultfilters import slugify

# Create your models here.


class category(models.Model):
    name=models.CharField(max_length=250,unique=True)




    class Meta:
        ordering = ('name',)
        verbose_name = 'categorys'
        verbose_name_plural = 'categoriess'

    def __str__(self):
        return '{}'.format(self.name)






class number(models.Model):
    date=models.DateField(default=date.today)

    number1=models.CharField(max_length=250,default="no:")
    number2=models.CharField(max_length=250,default="no:")
    number3=models.CharField(max_length=250,default="no:")
    categorys=models.ForeignKey(category,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.date)


