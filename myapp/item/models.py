from django.db import models

# Create your models here.

class Ingredient(models.Model):
    class Meta:
        app_label = 'item'
    INGREDIENT_EFFECT = (
        ('O', '유익함'),
        ('', '영향없음'),
        ('X', '유해'),
    )
    name = models.CharField(max_length=100, unique=True)
    oily = models.CharField(max_length=10, choices=INGREDIENT_EFFECT)
    dry = models.CharField(max_length=10, choices=INGREDIENT_EFFECT)
    sensitive = models.CharField(max_length=10,choices=INGREDIENT_EFFECT)
    def __str__(self):
        return self.name


class Product(models.Model):

    imageUrl = models.CharField(max_length=100)
    name = models.CharField(max_length=100, blank = True, unique=True)
    price = models.IntegerField()
    gender = models.CharField(max_length=20)
    category = models.CharField(max_length=50)
    ingredients = models.CharField(max_length = 254, blank = True)
    monthlySales = models.IntegerField()
    oilyScore = models.IntegerField(null=True,blank=True)
    dryScore = models.IntegerField(null=True,blank=True)
    sensitiveScore = models.IntegerField(null=True,blank=True)
    # connect_ingre = models.ManyToManyField(Ingredient,through='Connect',related_name="ingre_list",blank=True)
    # connect_ingre = models.ManyToManyField(Ingredient,related_name="ingre_list",blank=True)
    class Meta:
        app_label = 'item'
    def __str__(self):
        return self.name


# class Connect(models.Model):
#     product= models.ForeignKey(Product,on_delete=models.CASCADE)
#     product_name = models.CharField(max_length=100)
#     ingredient= models.ForeignKey(Ingredient,on_delete=models.CASCADE)
#     ingre_name = models.CharField(max_length=100)
