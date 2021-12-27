from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    cate_image= models.ImageField(verbose_name='Category Image', upload_to='products/', blank=True)
    cate_name=models.CharField(verbose_name='Category name', max_length=100)
    cate_shot_des = models.CharField(verbose_name='Category short description', max_length=200, blank=True)
    cate_des = models.TextField(verbose_name='Category description', blank=True)
    parent = models.ForeignKey('self', verbose_name='Parent Category',  on_delete=models.SET_NULL, blank=True, null=True, related_name='product_related')
    slug = models.SlugField(unique=True)
    code = models.CharField(verbose_name='Category code', max_length=50)
    is_active = models.BooleanField(verbose_name='Is Active', default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.cate_name
        
    def image_url(self):
        try:
            url=self.cate_image.url
        except:
            url=''
        return url


    def save(self, *args, **kwargs):
        self.slug = slugify(self.cate_name)
        return super().save(*args, **kwargs)

    def get_update_url(self):
        return reverse("ProductApp:category-update", kwargs={'slug':self.slug})

    def get_absolute_url(self):
        return reverse("ProductApp:category-detail", kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse("ProductApp:category-delete", kwargs={'slug':self.slug})
    

