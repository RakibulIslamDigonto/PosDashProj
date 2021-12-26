from django.db import models

# Create your models here.
class Category(models.Model):
    cate_image= models.ImageField(verbose_name='Category Image', upload_to='products/')
    cate_name=models.CharField(verbose_name='Category name', max_length=100)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='product_related')
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
