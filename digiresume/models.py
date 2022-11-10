
from django.db import models
from django.forms import ModelForm
# Create your models here.
class Me(models.Model):
    name = models.CharField(max_length=50, default='no name', null=True, blank=False)
    first = models.CharField(max_length=50, null=True, blank=False)
    title = models.CharField(max_length=50, null=True, blank=False)
    bio = models.TextField(max_length=1000, null=True, blank=False)

    profile_img = models.ImageField(upload_to='me', default='static/img/digiresume/user-thumb.jpg', null=True, blank=False)
    resume = models.FileField(upload_to='resume',null=True, blank=False)

    @property
    def my_resume(self):
        if resume:
            return resume
        else:
            return None

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Me'
        verbose_name_plural = 'Me'

class Clients(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    message = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class ClientsForm(ModelForm):
    class Meta:
        model = Clients
        fields = '__all__'

class CodingSkill(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    percentage = models.IntegerField(null=True,blank=True)
    image = models.ImageField(upload_to='digiresume/media/codingskills', null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Frameworks(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    percentage = models.IntegerField(null=True,blank=True)
    image = models.ImageField(upload_to='digiresume/media/codingskills', null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Portfolio(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    date_created = models.DateField(null=True)
    info = models.TextField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='digiresume/media/portfolios',null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Certificates(models.Model):
    title = models.CharField(max_length=50,null=True, blank=True)
    date_created = models.DateField(null=True)
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

class Testimonials(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    statement = models.CharField(max_length=50, null=True, blank=True)
    comment = models.TextField(max_length=200, null=True, blank=True)
    photo = models.ImageField(upload_to='digiresume/media/testimony', null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Blogs_Links(models.Model):
    row = models.CharField(max_length=500, null=True, blank=True)
    right_links = models.CharField(max_length=500, null=True, blank=True)
    left_links = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self) -> str:
        return self.row

