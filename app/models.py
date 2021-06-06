from django.db import models


# Create your models here.


class ShortURL(models.Model):
    main_url = models.URLField()
    short_url = models.URLField()
