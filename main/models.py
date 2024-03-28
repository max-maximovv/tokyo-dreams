from django.db import models

class inventory(models.Model):
    name = models.CharField('Name', max_length=100)
    type = models.CharField('Type of car', max_length=6)
    img_1 = models.ImageField(upload_to='sql_imgs/')
    img_2 = models.ImageField(upload_to='sql_imgs/')
    img_3 = models.ImageField(upload_to='sql_imgs/')
    img_4 = models.ImageField(upload_to='sql_imgs/')
    img_5 = models.ImageField(upload_to='sql_imgs/')
    img_6 = models.ImageField(upload_to='sql_imgs/')
    img_7 = models.ImageField(upload_to='sql_imgs/')
    img_8 = models.ImageField(upload_to='sql_imgs/')
    MSRP = models.CharField('msrp', max_length=40)
    Purchase = models.CharField('purchase', max_length=40)
    rent = models.CharField('rent', max_length=40)
    specs = models.TextField('specs')
    text = models.TextField('About car')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Inventory'
        verbose_name_plural = 'Inventories'
