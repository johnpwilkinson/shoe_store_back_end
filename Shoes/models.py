from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=140)
    website = models.URLField(max_length=150)

    def __str__(self):
        return self.name

class ShoeType(models.Model):
    style = models.CharField(max_length=50)

    def __str__(self):
        return self.style

class ShoeColor(models.Model):
    COLOR_CHOICES = [
        ('RED', 'Red'),
        ('ORANGE', 'Orange'),
        ('YELLOW', 'Yellow'),
        ('GREEN', 'Green'),
        ('BLUE', 'Blue'),
        ('INDIGO', 'Indigo'),
        ('VIOLET', 'Violet'),
        ('BLACK', 'Black'),
        ('WHITE', 'White')
    ]
    color_name = models.CharField(max_length=6, choices=COLOR_CHOICES)

    def __str__(self):
        return self.color_name
    
class Shoe(models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='made_by')
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE, related_name='color')
    material = models.CharField(max_length=50)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE, related_name='type')
    fasten_type = models.CharField(max_length=50)

    def __str__(self):
        return self.brand_name
