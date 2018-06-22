from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils.text import slugify
import json


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class ProductType(BaseModel):
    name = models.CharField(max_length=30, blank=False,  help_text='Name of product type up to 30 characters long.')
    slug = models.SlugField(unique=True)
    attributes = JSONField(default = json.dumps(dict({"data": []})))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_types')

    class Meta:
        ordering = ['name', ]

class Category(BaseModel):
    name = models.CharField(max_length=50, unique=True, help_text='Name for a main category up to 50 characters long.')
    product_type = models.ForeignKey(ProductType, related_name="categories", null=False, blank=False, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    class Meta:
        unique_together = ('product_type', 'name')
        verbose_name_plural = "categories"
        ordering = ['product_type', 'name', ]

    def __str__(self):
        return  self.name

    def get_absolute_url(self):
        return reverse('categories')


def pre_save_product_type_receiver(sender, instance, *arg, **kwargs):
    for key in kwargs.keys():
        print(key, kwargs[key])
    if instance.slug is None or instance.slug != slugify(instance.name):
        instance.slug = slugify(instance.name)

def pre_save_category_receiver(sender, instance, *arg, **kwargs):
    for key in kwargs.keys():
        print(key, kwargs[key])
    if instance.slug is None or instance.slug != slugify(instance.name):
        instance.slug = slugify(instance.name)

pre_save.connect(pre_save_category_receiver, sender=Category)
pre_save.connect(pre_save_product_type_receiver, sender=ProductType)

# Create your models here.
