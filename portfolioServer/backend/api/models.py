from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class ExampleModel(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Color(models.Model):
    HEX_COLOR_REGEX = r"^#(?:[0-9a-fA-F]{3}){1,2}$"
    color = models.CharField(
        max_length=7,
        validators=[
            RegexValidator(
                regex=HEX_COLOR_REGEX,
                message="Color must be a valid hexadecimal color code (e.g., #FFFFFF or #FFF).",
                code="invalid_hex_color",
            )
        ],
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.color