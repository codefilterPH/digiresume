
from django.db import models
from django.forms import ModelForm
from django.core.validators import EmailValidator
# Create your models here.
class Me(models.Model):
    name = models.CharField(max_length=50, default='no name', null=True, blank=False)
    first = models.CharField(max_length=50, null=True, blank=False)
    title = models.CharField(max_length=50, null=True, blank=False)
    bio = models.TextField(max_length=1000, null=True, blank=False)
    github = models.CharField(max_length=1000, null=True, blank=True)
    email = models.EmailField(max_length=150, null=True, blank=True, validators=[EmailValidator()])

    profile_img = models.ImageField(upload_to='me', default='static/img/digiresume/user-thumb.jpg', null=True, blank=False)
    resume = models.FileField(upload_to='resume',null=True, blank=False)

    date = models.DateTimeField(auto_now_add=True, null=True)

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

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

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

    class Meta:
        verbose_name = 'Coding skill'
        verbose_name_plural = 'Coding skills'

class Frameworks(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    percentage = models.IntegerField(null=True,blank=True)
    image = models.ImageField(upload_to='digiresume/media/codingskills', null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Framework'
        verbose_name_plural = 'Frameworks Learned'

class Portfolio(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    date_created = models.DateField(null=True)
    info = models.TextField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='digiresume/media/portfolios',null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'

class Certificates(models.Model):
    title = models.CharField(max_length=50,null=True, blank=True)
    date_created = models.DateField(null=True)
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'

class Testimonials(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    statement = models.CharField(max_length=50, null=True, blank=True)
    comment = models.TextField(max_length=200, null=True, blank=True)
    photo = models.ImageField(upload_to='digiresume/media/testimony', null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Testimony'
        verbose_name_plural = 'Testimonials'

class Blogs_Links(models.Model):
    row = models.CharField(max_length=500, null=True, blank=True)
    right_links = models.CharField(max_length=500, null=True, blank=True)
    left_links = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self) -> str:
        return self.row

