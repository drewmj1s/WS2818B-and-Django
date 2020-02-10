from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from math import sqrt
# Create your models here.
dx = .1





class Color(models.Model):

    red = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(255)])
    green = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(255)])
    blue = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(255)])
    brightness = models.IntegerField(default=255, validators=[MinValueValidator(0), MaxValueValidator(255)])


class Pattern(models.Model):
    name = models.CharField(max_length = 15, default = 'SOME-PATTERN', unique=True)
    back_and_forth = models.BooleanField(default = False)
    colors = models.CharField(default = "#FFF", max_length = 7, validators = [RegexValidator(r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$", "Give the hexidecimal value of this color")])
    num_leds = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(150)], default= 150)
    speed_var = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    #def get_absolute_url(self):
     #   return reverse('on_page', kwargs={"pattern_speed": self.speed_var, "pattern_color": self.colors, "pattern_name": self.name, })
        #return reverse('on_page', kwargs={"pattern": self})
#class Position(models.Model):




