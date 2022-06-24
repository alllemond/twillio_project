from django.db import models



class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50,primary_key=True, blank=True)

    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)

    def __str__(self):
       return self.title

    def save(self, *args, **kwargs):
       if not self.slug:
           self.slug= slugify(self.title)
       super().save(*args, **kwargs)
        
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = 'Categories'
