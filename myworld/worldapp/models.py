from django.db import models

# Create your models here.
class Recipes(models.Model):
	name = models.TextField(primary_key=True)
	preparation = models.TextField()

class Ingredients(models.Model):
	name = models.TextField(primary_key=True)

class Ingredient_Specs(models.Model):
	recipe_name = models.ForeignKey(Recipes)
	ingredient_name = models.ForeignKey(Ingredients)
	quantity = models.FloatField()
	unit = models.CharField(max_length=20)