from django.db import models

from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

class GalleryModel(models.Model):
    name = models.CharField(_('name'),max_length=100,)
    slug = models.SlugField(_('slug'),max_length=100,null=True,blank=True)
    description = models.TextField(_('description'),null=True, blank= True)
    image = models.ImageField(_('image'),blank=True,upload_to='images/%Y/%B/%d/%A')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
       
        super(GalleryModel, self).save(*args, **kwargs)
   
   
   
    def __str__(self) -> str:
        return self.name


