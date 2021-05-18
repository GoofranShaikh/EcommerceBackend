from django.db import models
from io import BytesIO    # resizing image
from PIL import Image     #pillow library to import image
from django.core.files import File
class category(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField()

    class Meta:
        ordering=('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'   # 'f'--> format obeject.slug---->(where slug is used for url)

class products(models.Model):
    category=models.ForeignKey(category,related_name='products' , on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    slug=models.SlugField()
    description=models.TextField(blank=True,null=True)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    image=models.ImageField(upload_to='uploads/',blank=True,null=True)
    thumbnail=models.ImageField(upload_to='uploads/',blank=True,null=True)
    dateCreated=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('-dateCreated',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.category}/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' +self.thumbnail.url
        else:
            if self.image:
                self.thumbnail=self.make_thumbnail(self.image)
                self.save()
                return 'http://127.0.0.1:8000'+ self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image , size=(300,400)):
        img=Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io= BytesIO()
        img.save(thumb_io,'JPEG',quality=85)
        thumbnail=File(thumb_io,name=image.name)
        return thumbnail


    
    
