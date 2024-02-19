from django.db import models

# Create your models here.
class IndexPage(models.Model):
    banner = models.CharField(max_length=200, unique=False, default='مرحبا بكم')
    slag = models.CharField(max_length=200, default='التعلم يبداء من مقال')
    logo = models.ImageField(upload_to='media/index_photos/', default='index_photos/LOGO.jpg')
    logoalt = models.CharField(max_length=200, default='logo img')
    supslag = models.CharField(max_length=500, default='أبداء رحلتك بالتعلم العميق و المفيد بتصفح احدى مقالتنا')

    def __str__(self):
        return self.banner


class aboutPage(models.Model):
    title = models.CharField(max_length=200, default='ما هو هدفنا ولماذا نطمح للوصول لكل العرب؟')
    text1 = models.CharField(max_length=700, default='لدينا هدف واحد وهو ان نثري المحتوى العربي بالمعلومات المفيدة وزيادة حجم المشاركة للمعلومات باللغة العربية')
    photo1 = models.ImageField(upload_to='media/about_photos/', default='about_photos/LOGO.jpg')
    photo1alt = models.CharField(max_length=200, default='about img')

    def __str__(self):
        return self.title